import subprocess
from typing import Optional

def run_python_file(file_path: str) -> subprocess.CompletedProcess:
    """
    Executes a Python script and captures its stdout and stderr.

    Args:
        file_path: The path to the Python script to execute.

    Returns:
        A subprocess.CompletedProcess object containing the result of the execution.
        The stdout and stderr attributes will contain the output as text.
    """
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            check=False # Do not raise CalledProcessError, allow returncode to indicate success/failure
        )
        return result
    except FileNotFoundError:
        error_msg = f"Error: 'python' command not found. Ensure Python is installed and in PATH."
        return subprocess.CompletedProcess(args=["python", file_path], returncode=1, stdout="", stderr=error_msg)
    except Exception as e:
        error_msg = f"An unexpected error occurred while running the script: {e}"
        return subprocess.CompletedProcess(args=["python", file_path], returncode=1, stdout="", stderr=error_msg)
