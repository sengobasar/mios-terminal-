import re


def parse_error(error_text: str):
    """
    Parse terminal errors and return structured diagnosis.
    """

    error_text = error_text.strip()

    # -------------------------------
    # Missing Python module
    # -------------------------------
    if "ModuleNotFoundError" in error_text or "ImportError" in error_text:

        # try extracting module name
        match = re.search(r"named ['\"]?([^'\"]+)['\"]?", error_text)

        if match:
            package = match.group(1)
        else:
            # fallback extraction
            parts = error_text.split(":")
            package = parts[-1].strip()

        return {
            "type": "missing_package",
            "package": package
        }

    # -------------------------------
    # Command not found
    # -------------------------------
    if "command not found" in error_text or "is not recognized as an internal or external command" in error_text:

        match = re.search(r"'(.+?)'", error_text)

        command = match.group(1) if match else "unknown"

        return {
            "type": "missing_command",
            "command": command
        }

    # -------------------------------
    # Permission errors
    # -------------------------------
    if "Permission denied" in error_text:

        return {
            "type": "permission_error"
        }

    # -------------------------------
    # Pip dependency conflict
    # -------------------------------
    if "ResolutionImpossible" in error_text or "dependency conflict" in error_text:

        return {
            "type": "dependency_conflict"
        }

    # -------------------------------
    # Unknown error
    # -------------------------------
    return {
        "type": "unknown",
        "message": error_text
    }