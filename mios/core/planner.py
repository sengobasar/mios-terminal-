import json

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

    return {
        "action": "none"
    }
