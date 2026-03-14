from typing import List, Dict, Any
from mios.core.llm_planner import generate_llm_plan
from mios.memory.error_memory import lookup_error_solution
import re


def extract_missing_package(error_message: str):
    """
    Extracts the missing package name from a ModuleNotFoundError message.
    """
    match = re.search(r"No module named '(\w+)'", error_message)
    if match:
        return match.group(1)
    return None

def generate_plan(problem: str, file_path: str = None) -> List[Dict[str, Any]]:
    """
    Generates a repair plan for the given problem.
    First checks memory for known solutions, then uses LLM planning if no match found.
    """
    solution = lookup_error_solution(problem)
    if solution:
        return [
            {"action": "run_command", "command": solution},
            {"action": "retry_command"}
        ]
    
    return generate_llm_plan(problem, file_path)
