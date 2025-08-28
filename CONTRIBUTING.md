# Contributing Guidlines

We kindly request that for any suggested change to:

1. Fork the repository
2. Clone your fork locally
3. Create a new branch (please use a descriptive name)
4. Make changes
5. Test your changes
6. Commit your changes with clear commit messages
7. Push your branch to your forked repository
8. Open a pull request
9. Respond to feedback
10. Keep your branch updated

## Suggesting updates for `SMARTS-RX`

If you have suggestions for `SMARTS-RX`, you can provide your suggestions in [SMARTS_RX.txt](./SMARTS_RX.txt).  
To update [smarts_rx.json](./smarts_rx.json) and [README.md](./README.md) follow the instructions below to setup the Python environment and use the provided code.

## Setting Up the Python Environment

To use the provided code for updating `smartsrx`, follow these steps to set up the Python environment:

### Prerequisites
Ensure you have the following installed:
- Python 3.9 or later (recommended version: 3.10)
- `poetry` 2.1.3 (Python package manager)

***Note:** You can either create this base environment manually or create a `conda` environment with `smartsrx-env.yml`.*

### Steps to Set Up
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your_github_space>/smartsrx.git
   cd smartsrx
   ```
2.  **Install Dependencies**:
    ```bash
    poetry install
    ```
3. **Verify Installation**:
    ```bash
    python -m pip list --format=freeze
    ```

### Generate `smartsrx.json`:
1. Update `SMARTS_RX.txt`
2. Run the script:
   ```bash
   python -m smartsrx.create_json
   ```

### Update the README Table:
1. After updating `SMARTS_RX.txt` and generating the JSON file:
2. Run the table update script:
   ```bash
   python -m smartsrx.update_readme_table
   ```
   This will automatically extract class, subclass, and `SMARTS-RX` information from the `SMARTS_RX.txt` file and update the table below.
