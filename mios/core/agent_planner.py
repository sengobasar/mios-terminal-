import re
from typing import List, Dict, Any

def _extract_package_name_from_error(error_message: str) -> str | None:
    """
    Extracts the missing package name from a ModuleNotFoundError message.
    """
    match = re.search(r"No module named '(\w+)'", error_message)
    if match:
        return match.group(1)
    return None

def generate_plan(problem: str) -> List[Dict[str, Any]]:
    """
    Generates a plan based on the problem description.
    Each step in the plan is a dictionary representing an action and its parameters.
    """
    plan: List[Dict[str, Any]] = []

    if "ModuleNotFoundError" in problem:
        package_name = _extract_package_name_from_error(problem)
        plan.append({"action": "analyze_error", "error_message": problem})
        # The environment detection is implicitly handled by build_world_state in the loop,
        # but a specific analysis action might be useful.
        # plan.append({"action": "detect_environment"})

        if package_name:
            plan.append({"action": "install_package", "package": package_name})
            plan.append({"action": "retry_command"}) # Assuming the original command will be retried after install
        else:
            # If package name cannot be extracted, suggest a generic analysis or manual intervention
            plan.append({"action": "suggest_manual_dependency_install", "reason": "Could not parse missing package from error."})
    else:
        plan.append({"action": "analyze_problem", "problem_description": problem})
        # Add a default action if no specific error is detected, e.g., "suggest_initial_approach"
        # plan.append({"action": "suggest_initial_approach", "approach": "Reviewing the problem statement and context."})

    return plan
