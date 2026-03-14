from typing import Dict, Any

def observe(result: Any) -> Dict[str, Any]:
    """
    Observes the result of a command execution, extracting stdout, stderr,
    and detecting if an error occurred.

    Args:
        result: An object representing the outcome of a command execution.
                It is expected to have 'stdout' (str), 'stderr' (str),
                and 'returncode' (int) attributes.

    Returns:
        A dictionary containing:
        - 'stdout': The standard output of the command.
        - 'stderr': The standard error of the command.
        - 'error_detected': True if an error was detected (non-zero return code), False otherwise.
    """
    stdout = result.stdout if hasattr(result, 'stdout') else ""
    stderr = result.stderr if hasattr(result, 'stderr') else ""
    error_detected = hasattr(result, 'returncode') and result.returncode != 0

    return {
        "stdout": stdout,
        "stderr": stderr,
        "error_detected": error_detected
    }
