import re
from typing import List, Dict, Any
from mios.tools.error_parser import parse_python_error
from mios.memory.error_memory import lookup_error_solution

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
    
    solution = lookup_error_solution(problem)
    if solution:
        return [
            {"action": "run_command", "command": solution},
            {"action": "retry_command"}
        ]

    parsed_error = parse_python_error(problem)
    if parsed_error["type"] == "missing_module":
        missing_module = parsed_error["module"]
        return [
            {
                "action": "edit_file",
                "file": "current_script",
                "old_text": missing_module,
                "new_text": missing_module
            },
            {
                "action": "install_package",
                "package": missing_module
            },
            {
                "action": "retry_command"
            }
        ]
    # Fallback for other types of errors or when no specific error is detected
    elif "ModuleNotFoundError" in problem: # Keep original fallback for ModuleNotFoundError if parser fails
        package_name = _extract_package_name_from_error(problem)
        if package_name:
            return [
                {"action": "install_package", "package": package_name},
                {"action": "retry_command"}
            ]
    
    # Default plan if no specific error is handled
    plan.append({"action": "analyze_problem", "problem_description": problem})
    return plan
