"""
README Table Generator for Reactive Functions

This module provides utilities to automatically update the reactive functions table
in README.md with the latest data from the source file. This ensures documentation
stays synchronized with the actual data.

The script performs the following operations:
1. Reads reactive function data from the file (first 3 columns)
2. Generates a properly formatted Markdown table
3. Locates and replaces the existing table section in README.md
4. Preserves HTML comments and formatting structure

Table Structure:
    - Class: Top-level category classification
    - Subclass: Mid-level subcategory classification
    - smartsrx key: Specific type identifier (SMARTS-RX)

The script uses regex patterns to locate the table section and includes fallback
mechanisms for different README.md formatting variations.

Usage:
    Run this script directly from the project root directory:
    $ python -m smartsrx.update_readme_table
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple


def update_readme_table(readme_path: str, file_path: str, sep: str, header: bool = True) -> bool:
    # pylint: disable=too-many-locals
    """
    Update the reactive functions table in README.md with current `SMARTS-RX`data.

    This function performs a complete table replacement operation:
    1. Parses the file to extract category, subcategory, and `SMARTS-RX` data
    2. Generates a properly formatted Markdown table
    3. Locates the existing table section using regex patterns
    4. Replaces the old table with the updated version

    The function preserves HTML comments and handles multiple README.md formats
    through primary and fallback regex patterns.

    Args:
        readme_path: Absolute or relative path to the README.md file
        file_path: Absolute or relative path to the data file
        sep: Delimiter used in the data file (e.g., "\t" for TSV)
        header: Whether the data file includes a header row (default: True)

    Returns:
        True if the table was successfully updated, False if the table
        section could not be located or updated

    Raises:
        FileNotFoundError: If either the README.md or file cannot be found
        IOError: If there are issues reading from or writing to the files

    Example:
        >>> success = update_readme_table("README.md", "data.tsv", "\t")
        >>> if success:
        ...     print("Table updated successfully")
    """
    # Read the TSV file
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    if header:
        lines = lines[1:]

    # Extract the first three columns from each line, skipping comments and empty lines
    table_data: List[Tuple[str, str, str]] = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split(sep)
        if len(parts) >= 3:
            table_data.append((parts[0], parts[1], parts[2]))

    # Read the README.md file
    with open(readme_path, "r", encoding="utf-8") as f:
        readme_content = f.read()

    # Create the new table content
    table_header = "| Class | Subclass | `SMARTS-RX` |\n|:------:|:--------:|:----------:|\n"
    table_rows = "\n".join(
        [f"| {category} | {subcategory} | {smarts_rx} |" for category, subcategory, smarts_rx in table_data]
    )
    new_table = table_header + table_rows + "\n"

    # Find the section with the introduction text and the table
    # This matches the intro line, the HTML comment, and any existing table until the next heading or EOF
    intro_pattern = (
        r"(Below we list classes and subclasses for the current `smartsrx` version \(v[\d\.]+\):)\s*\n"
        r"(<!-- The table will be populated by the update_readme_table\.py script -->)\s*\n\n([\s\S]*?)(?=\n\n#|$)"
    )
    match = re.search(intro_pattern, readme_content)

    if match:
        intro_text = match.group(1)  # The introductory text
        comment_line = match.group(2)  # The HTML comment
        start_idx = match.start()
        end_idx = match.end()

        # Create the new section with the updated table, preserving the comment
        new_section = f"{intro_text}\n{comment_line}\n\n{new_table}"

        # Replace the old section with the new one
        updated_readme = readme_content[:start_idx] + new_section + readme_content[end_idx:]

        # Write the updated content back to README.md
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_readme)

        print(f"README.md has been updated with {len(table_data)} entries in the table.")
        return True

    # As a fallback, try a more flexible pattern that might not include the comment
    fallback_pattern = (
        r"(Below we list classes and subclasses for the current `smartsrx` version \(v[\d\.]+\):)\s*\n\n"
        r"([\s\S]*?)(?=\n\n#|$)"
    )
    fallback_match = re.search(fallback_pattern, readme_content)

    if fallback_match:
        intro_text = fallback_match.group(1)
        start_idx = fallback_match.start()
        end_idx = fallback_match.end()

        # Create the new section with the updated table, adding the comment if it wasn't there
        new_section = (
            f"{intro_text}\n<!-- The table will be populated by the update_readme_table.py script -->\n\n{new_table}"
        )

        # Replace the old section with the new one
        updated_readme = readme_content[:start_idx] + new_section + readme_content[end_idx:]

        # Write the updated content back to README.md
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_readme)

        print(f"README.md has been updated with {len(table_data)} entries in the table (using fallback method).")
        return True

    print("Could not find the table section in README.md")
    return False


def main():
    """
    Main function to orchestrate the README.md table update process.

    This function handles the complete workflow:
    1. Determines the correct file paths relative to the project structure
    2. Validates that required input files exist
    3. Calls the table update function with proper error handling
    4. Provides user feedback on success or failure

    The function automatically locates files based on the script's position
    in the project directory structure, making it safe to run from anywhere
    within the project.

    Project Structure Expected:
        project_root/
        ├── README.md
        ├── SMARTS_RX.txt
        └── smartsrx/
            └── update_readme_table.py

    Exit Codes:
        0: Success - table updated successfully
        1: Failure - missing files or update failed

    Example:
        >>> main()
        README.md has been updated with 150 entries in the table.
    """
    # Find project root directory (where README.md is located)
    script_path = Path(__file__).resolve()
    package_dir = script_path.parent
    project_dir = package_dir.parent

    # Define paths
    readme_path = project_dir / "README.md"
    file_path = project_dir / "SMARTS_RX.txt"

    # Check if files exist
    if not readme_path.exists():
        print(f"Error: README.md not found at {readme_path}")
        sys.exit(1)

    if not file_path.exists():
        print(f"Error: SMARTS_RX.txt not found at {file_path}")
        sys.exit(1)

    # Update the table
    success = update_readme_table(readme_path.as_posix(), file_path.as_posix(), sep=" ")
    if not success:
        sys.exit(1)


if __name__ == "__main__":
    main()
