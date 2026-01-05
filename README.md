# Bulk File Organizer

A powerful and customizable command-line utility built with Python to help you automatically organize files in any directory. This tool scans a specified folder (like a cluttered 'Downloads' folder) and intelligently moves files into subdirectories based on their type (e.g., images, documents, videos), bringing order to chaos in seconds.

## Features

*   **Customizable Rules**: Easily define your own organization rules by editing a simple `config.json` file. No need to modify the Python code to add new file types or change destination folders.
*   **Automatic Folder Creation**: Destination folders (e.g., 'Images', 'Documents') are created automatically if they don't already exist.
*   **Intelligent Conflict Resolution**: If a file with the same name already exists in the destination folder, the script won't crash or overwrite. It will intelligently rename the new file (e.g., `report (1).pdf`).
*   **Safety First with Dry-Run Mode**: Preview all file operations without making any actual changes using the `--dry-run` flag. This lets you see what will happen before you commit.
*   **Comprehensive Logging**: A detailed `organizer.log` file is created, recording every action the script takes, from successful moves to warnings and errors. This provides a full audit trail.
*   **User-Friendly Progress Bar**: For large directories, a real-time progress bar shows you the status of the organization process, so you're never left guessing.
*   **Robust Error Handling**: The script is designed to handle common issues gracefully, such as missing configuration files or permission errors during file moves, providing clear feedback instead of crashing.
*   **Simple Command-Line Interface (CLI)**: A clean and simple interface allows you to specify the target directory and options directly from your terminal.

## Installation 
Follow below Steos for instaltion in your local. This guide assumes you have Python 3 installed and are comfortable with the command line.

1. **Clone the Repo:** 
    ```sh
    git clone <my link>
    ```
    ```sh
    cd <folder name>
    ```

2. **Create Python Virtual Env**
    ```sh
    # This command creates a new directory named 'venv' for the virtual environment
    python -m venv vnev
    ```

3.  **Activate the Virtual Environment**

    Before you can install packages into the virtual environment, you must activate it. The command differs depending on your operating system.

    *   **On Windows:**
        ```sh
        venv\Scripts\activate
        ```
    *   **On macOS and Linux:**
        ```sh
        source venv/bin/activate
        ```
    After activation, you should see `(venv)` at the beginning of your command prompt.

4.  **Install Required Dependencies**

    This project has one external dependency, `tqdm`, which is used to display the progress bar. Use `pip`, Python's package installer, to install it.

    ```sh
    # This command will download and install the tqdm library into your active virtual environment
    pip install -r requirements.txt
    ```

    You are now ready to run the application!

## Usage

Once the installation is complete, you can run the Bulk File Organizer from your terminal. Make sure your virtual environment is still activated.

### Basic Organization

To run the script and organize a directory, provide the path to the target directory as the main argument.

**Warning:** This command will make changes to your file system. It is highly recommended to run a `dry-run` first (see below).

```sh
# Replace '/path/to/your/downloads' with the actual path to the folder you want to clean up.
python organizer.py /path/to/your/downloads
