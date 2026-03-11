import json
from mios.debug.error_parser import parse_error

def plan_from_error(error):
    """
    Convert error analysis into an action plan.
    """

    analysis = parse_error(error)

    if analysis["type"] == "missing_package":
        return {
            "action": "install_package",
            "package": analysis["package"]
        }

    elif analysis["type"] == "missing_command":
        return {
            "action": "suggest_install_command",
            "command": analysis["command"]
        }

    elif analysis["type"] == "permission_error":
        return {
            "action": "suggest_run_with_sudo",
            "command": analysis["command"]
        }

    elif analysis["type"] == "missing_file":
        return {
            "action": "suggest_check_file_path",
            "file": analysis["file"]
        }

    return {
        "action": "none"
    }
