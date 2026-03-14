import re

def parse_python_error(stderr: str):
    """
    Parses Python error output to detect specific error types and extract relevant information.
    Currently supports detecting ModuleNotFoundError.
    """
    # Detect ModuleNotFoundError
    module_not_found_match = re.search(r"ModuleNotFoundError: No module named '([^']+)'", stderr)
    if module_not_found_match:
        module_name = module_not_found_match.group(1)
        return {
            "type": "missing_module",
            "module": module_name
        }

    # Add other error parsing logic here in the future

    return {"type": "unknown"}
