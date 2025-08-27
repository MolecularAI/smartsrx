"""
SMARTS-RX Example: Substructure Matching with RDKit FilterCatalog

This example demonstrates how to use the SMARTS-RX JSON database with RDKit's
FilterCatalog for efficient substructure matching and molecular fingerprinting.

The script performs the following operations:
1. Loads the SMARTS-RX JSON database containing reactive function SMARTS patterns
2. Creates an RDKit FilterCatalog from the SMARTS patterns for fast matching
3. Searches a target molecule for substructure matches
4. Generates an SMARTS-RX fingerprint as a sorted list of matching identifiers

Key Components:
    - JSON database loading and parsing
    - RDKit FilterCatalog construction for batch SMARTS matching
    - Molecular substructure identification
    - Fingerprint generation for chemical analysis

Dependencies:
    - RDKit: For molecular processing and substructure matching
    - JSON: For database loading
    - smartsrx.json: The reactive function database file

Usage:
    Ensure smartsrx.json is in the same directory and run:
    $ python smartsrx_example.py

Example Output:
    Acid_Aromatic Alcohol_Primary
"""

import json

from rdkit import Chem
from rdkit.Chem import FilterCatalog


def main():
    # pylint: disable=no-member
    """Main function to demonstrate SMARTS-RX substructure matching with RDKit.
    This function orchestrates the loading of the SMARTS-RX database, creation of
    the FilterCatalog, and performs substructure matching on a target molecule.
    """
    # Configuration
    smartsrx_file = "smartsrx.json"

    # Load the SMARTS-RX reactive function database
    with open(smartsrx_file, "rt", encoding="utf-8") as read_file:
        smartsrx_library_json = json.load(read_file)

    # Create RDKit FilterCatalog as a library of SMARTS patterns
    # FilterCatalog provides efficient batch substructure matching
    filter_catalog = FilterCatalog.FilterCatalog()

    for entry in smartsrx_library_json["data"]:
        smartsrx = entry["specific_type"]  # The SMARTS-RX identifier
        smarts = entry["smarts"]  # The SMARTS pattern string

        # Create RDKit molecule object from SMARTS pattern
        mol_pattern = Chem.MolFromSmarts(smarts)

        # Create SMARTS matcher for this pattern
        smarts_matcher = FilterCatalog.SmartsMatcher(mol_pattern)

        # Add entry to FilterCatalog with SMARTS-RX as identifier
        catalog_entry = FilterCatalog.FilterCatalogEntry(smartsrx, smarts_matcher)
        filter_catalog.AddEntry(catalog_entry)

    # Example: Search for reactive functional groups in a target molecule
    target_smiles = "C1C(C(O)C)=CC=C(C(O)C)C=1.Cl"

    # Convert SMILES to RDKit molecule object and perform substructure matching
    target_molecule = Chem.MolFromSmiles(target_smiles)
    matches = filter_catalog.GetMatches(target_molecule)

    # Extract SMARTS-RXs from matches and sort for consistent fingerprinting
    smartsrx = [match.GetDescription() for match in matches]
    smartsrx.sort()

    # Generate and display the SMARTS-RX fingerprint
    # This represents the reactive functional groups present in the molecule
    # Example: Expected ooutput should be 'SecondaryAlcoholMixAcyclic'
    print(" ".join(smartsrx))


if __name__ == "__main__":
    main()
