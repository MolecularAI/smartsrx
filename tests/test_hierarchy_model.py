import pytest

from smartsrx import ReactiveFunction, ReactiveFunctionDatabase


@pytest.fixture
def sample_tsv_data():
    """Fixture providing sample TSV data for testing"""
    return [
        "Acid\tCarboxylicAcid\tAcid_Aromatic\tc[CX3](=[OX1])[OX2H,OX1-]\n",
        "Alcohol\tPrimaryAlcohol\tAlcohol_Primary\t[CX4;!$(C(O)(O));!$(C([#6]=[#8])O)][OX2H]\n",
        "# This is a comment line that should be ignored\n",
        "Alcohol\tSecondaryAlcohol\tAlcohol_Secondary\t[CX4][CX4;!$(C(O)(O));!$(C([#6]=[#8])O)][OX2H]\n",
        "\n",  # Empty line that should be ignored
        "Malformed line",  # Malformed line that should be ignored
    ]


@pytest.fixture
def test_db(sample_tsv_data):
    """Fixture creating a test database from the sample data"""
    return ReactiveFunctionDatabase.from_lines(sample_tsv_data, "\t", "1.0.0")


def test_database_initialization(test_db):
    """Test that the database initializes correctly from TSV data"""
    assert test_db.version == "1.0.0"
    # There are 3 entries grouped in 2 categories
    assert len(test_db.data) == 3
    assert len(test_db.categories) == 2
    assert len(test_db.subcategories) == 3
    assert len(test_db.specific_types) == 3

    # Check that categories are created correctly
    assert "Acid" in test_db.categories
    assert "Alcohol" in test_db.categories

    # Check subcategories
    assert "CarboxylicAcid" in test_db.subcategories
    assert "PrimaryAlcohol" in test_db.subcategories
    assert "SecondaryAlcohol" in test_db.subcategories

    # Verify specific types
    assert "Acid_Aromatic" in test_db.specific_types


def test_get_function(test_db):
    """Test retrieving a function using the hierarchical path"""
    # Valid function retrieval
    for term in ["Acid", "Alcohol"]:
        results = test_db.get_function(term)
        assert isinstance(results, list)
        if term == "Acid":
            assert len(results) == 1
        elif term == "Alcohol":
            assert len(results) == 2
        for entry in results:
            assert isinstance(entry, ReactiveFunction)

    # Non-existent paths should return None
    for term in ["InvalidCategory", "InvalidSubCategory", "InvalidType"]:
        assert test_db.get_function(term) == []


def test_search_smartsrx(test_db):
    """Test searching for SMARTS-RX"""
    # Valid search
    acid_aromatic = test_db.search_smartsrx("Acid_Aromatic")
    assert isinstance(acid_aromatic, ReactiveFunction)
    assert acid_aromatic.category == "Acid"
    assert acid_aromatic.subcategory == "CarboxylicAcid"
    assert acid_aromatic.specific_type == "Acid_Aromatic"
    assert acid_aromatic.smarts == "c[CX3](=[OX1])[OX2H,OX1-]"

    # Search for alcohol types
    alcohol_primary = test_db.search_smartsrx("Alcohol_Primary")
    assert isinstance(alcohol_primary, ReactiveFunction)
    assert alcohol_primary.category == "Alcohol"
    assert alcohol_primary.subcategory == "PrimaryAlcohol"
    assert alcohol_primary.specific_type == "Alcohol_Primary"
    assert alcohol_primary.smarts == "[CX4;!$(C(O)(O));!$(C([#6]=[#8])O)][OX2H]"

    # Non-existent key should return None
    assert test_db.search_smartsrx("NonExistentKey") is None


def test_empty_database():
    """Test creating an empty database"""
    empty_db = ReactiveFunctionDatabase.from_lines([], "\t", "0.0.1")
    assert empty_db.version == "0.0.1"
    assert empty_db.data == []
    assert empty_db.categories == []
    assert empty_db.subcategories == []
    assert empty_db.specific_types == []
    # Any search should return None
    for term in ["Any", "Category", "Type"]:
        assert empty_db.get_function(term) == []
    assert empty_db.search_smartsrx("Any_Key") is None


def test_malformed_data_handling():
    """Test that malformed data is handled gracefully"""
    malformed_data = [
        "Category\tSubCategory\tSpecificType\n",  # Missing columns
        "Category\tSubCategory\n",  # Even more missing columns
        "\t\t\t\t\t\n",  # Empty fields
    ]

    # Should not raise exceptions
    db = ReactiveFunctionDatabase.from_lines(malformed_data, "\t", "1.0.0")
    assert db.data == []
    assert db.categories == []
    assert db.subcategories == []
    assert db.specific_types == []
