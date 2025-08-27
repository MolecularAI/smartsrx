"""
Hierarchical Database Models for Reactive Functions

This module defines Pydantic models and utilities for managing a hierarchical database
of reactive functional groups used in chemical analysis and molecular processing.

Models:
    ReactiveFunction: Represents individual reactive functional group details
    ReactiveFunctionDatabase: Manages collections of reactive functions with search capabilities

The database supports three-level hierarchy searches by:
    - Category (top-level classification)
    - Subcategory (mid-level classification)
    - Specific type (SMARTS-RX - bottom-level identifier)

Data is typically loaded from TSV-formatted input files containing SMARTS patterns
and associated metadata for each reactive function.
"""

from typing import List, Optional

from pydantic import BaseModel, Field


class ReactiveFunction(BaseModel):
    """
    Model representing a reactive functional group with its associated metadata.

    This model encapsulates all the information needed to identify and work with
    a reactive functional group, including its hierarchical classification and
    SMARTS pattern definitions.

    Attributes:
        category: Top-level classification (e.g., "Electrophile", "Nucleophile")
        subcategory: Mid-level classification for more specific grouping
        specific_type: Bottom-level identifier (SMARTS-RX) for exact function type
        smarts: SMARTS pattern string for molecular matching
    """

    category: str = Field(..., description="Category of the reactive function")
    subcategory: str = Field(..., description="Subcategory of the reactive function")
    specific_type: str = Field(..., description="Specific type of the reactive function")
    smarts: str = Field(..., description="SMARTS pattern")


class ReactiveFunctionDatabase(BaseModel):
    """Database of reactive functions organized in a three-level hierarchy"""

    version: str = Field(..., description="Version of the SMARTS database")
    data: List[ReactiveFunction] = Field(
        ...,
        description="Collection of reactive functions",
    )

    @property
    def categories(self) -> List[str]:
        """List of all categories in the database"""
        return list({function.category for function in self.data})

    @property
    def subcategories(self) -> List[str]:
        """List of all subcategories in the database"""
        return list({function.subcategory for function in self.data})

    @property
    def specific_types(self) -> List[str]:
        """List of all specific types (SMARTS-RXs) in the database"""
        return list({function.specific_type for function in self.data})

    def get_function(self, query: str) -> List[ReactiveFunction]:
        """
        Retrieve a reactive function by searching across all hierarchy levels.

        Searches through category, subcategory, and specific_type fields to find
        the first matching reactive function. The search is case-sensitive and
        looks for exact matches.

        Args:
            query: Search term to match against category, subcategory, or specific_type

        Returns:
            All matching ReactiveFunction, or empty list if no match is found

        Example:
            >>> func = db.get_function("Acid")  # Search by category
            >>> func = db.get_function("Acid_Aromatic")  # Search by specific_type
        """
        matching_functions = []
        for function in self.data:
            if query in [function.category, function.subcategory, function.specific_type]:
                matching_functions.append(function)

        return matching_functions

    def search_smartsrx(self, query: str) -> Optional[ReactiveFunction]:
        """
        Search for a reactive function by its specific SMARTS-RX identifier.

        This method specifically searches the specific_type field, which contains
        the SMARTS-RX identifiers. It performs case-sensitive exact matching.

        Args:
            query: The SMARTS-RX (specific_type) to search for

        Returns:
            The matching ReactiveFunction, or None if no SMARTS-RX matches

        Example:
            >>> func = db.search_azkeys("Acid_Aromatic")
            >>> if func:
            ...     print(f"Found: {func.category} - {func.subcategory}")
        """
        for function in self.data:
            if function.specific_type == query:
                return function

        return None

    @classmethod
    def from_lines(cls, lines: List[str], sep: str, version: str) -> "ReactiveFunctionDatabase":
        """
        Create a database instance from `sep`-formatted input lines.

        Parses separated values where each line represents a reactive function.
        Empty lines and lines starting with '#' are treated as comments and skipped.
        Lines with fewer than 6 columns are considered malformed and ignored.

        Expected `sep` format:
            category<sep>subcategory<sep>specific_type<sep>smarts

        Args:
            lines: List of `sep`-formatted strings to parse`
            sep: Delimiter used in the input lines (e.g., "\t" for TSV)
            version: Version identifier to assign to the database

        Returns:
            New ReactiveFunctionDatabase instance populated with parsed data

        Example:
            >>> with open('reactive_functions.tsv', 'r') as f:
            ...     lines = f.readlines()
            >>> db = ReactiveFunctionDatabase.from_lines(lines, "\t", "v2.1")
        """
        data: List[ReactiveFunction] = []

        for line in lines:
            if not line.strip() or line.startswith("#"):  # Skip empty lines and comments
                continue

            parts = line.strip().split(sep)
            # The file is expected to have at least 4 columns
            # category, subcategory, specific_type, smarts
            if len(parts) < 4:
                continue  # Skip malformed lines

            category, subcategory, specific_type, smarts = parts[:4]

            data.append(
                ReactiveFunction(
                    category=category,
                    subcategory=subcategory,
                    specific_type=specific_type,
                    smarts=smarts,
                )
            )

        return cls(version=version, data=data)
