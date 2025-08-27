"""
JSON Database Generator for Reactive Functions

This module provides utilities to convert TSV-formatted reactive function data into
structured JSON files for distribution and consumption by other applications.

The script performs the following operations:
1. Reads reactive function data from a TSV input file
2. Extracts version information from pyproject.toml
3. Creates a hierarchical database using ReactiveFunctionDatabase model
4. Generates two output files:
   - smartsrx_schema.json: JSON schema definition for validation
   - smartsrx.json: Complete hierarchical database in JSON format

Input Requirements:
    - SMARTS_RX.txt: TSV file with reactive function data
    - pyproject.toml: Project configuration file with version information

Output Files:
    - smartsrx_schema.json: Pydantic-generated JSON schema for the database
    - smartsrx.json: Complete database in JSON format ready for distribution

Usage:
    Run this script directly from the project root directory:
    $ python -m smartsrx.create_json
"""

import json

import toml

from smartsrx.hierarchy_model import ReactiveFunctionDatabase


def main():
    """
    Main function to generate JSON database and schema files from `SMARTS_RX.txt`.

    This function orchestrates the complete conversion process:
    1. Loads reactive function data from the `SMARTS_RX.txt` file
    2. Extracts version information from pyproject.toml (with fallback)
    3. Generates JSON schema file for validation purposes
    4. Creates and exports the complete database as JSON

    The function handles missing files gracefully by using default values
    and provides console feedback on successful completion.

    Raises:
        FileNotFoundError: If the required `SMARTS_RX.txt` file is not found
        json.JSONEncodeError: If there are issues serializing the data

    Example:
        >>> main()
        Database created successfully!
    """
    # Load the data from file
    with open("./SMARTS_RX.txt", "rt", encoding="utf-8") as f:
        lines = f.readlines()
        # Skip header line
        lines = lines[1:]

    # Load version from pyproject.toml
    try:
        with open("./pyproject.toml", "rt", encoding="utf-8") as f:
            pyproject_data = toml.load(f)
            version = pyproject_data["project"]["version"]
    except FileNotFoundError:
        version = "1.0.0"  # Default version if pyproject.toml is not found
    except KeyError:
        version = "1.0.0"  # Default version if version is not found in pyproject.toml

    # Write JSON Schema file
    with open("smartsrx_schema.json", "wt", encoding="utf-8") as json_file:
        json.dump(ReactiveFunctionDatabase.model_json_schema(), json_file, indent=2)

    # Create the database
    db = ReactiveFunctionDatabase.from_lines(lines, sep=" ", version=version)

    # Convert to JSON
    with open("smartsrx.json", "wt", encoding="utf-8") as json_file:
        json.dump(db.model_dump(), json_file, indent=2)

    print("Database created successfully!")


if __name__ == "__main__":
    main()
