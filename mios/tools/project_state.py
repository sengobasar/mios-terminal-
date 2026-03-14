import os
import subprocess
from typing import Dict, Any

from mios.tools.environment_detector import detect_python_environment

def _detect_project_type() -> str:
    """
    Detects the project type based on common file indicators.
    """
    if os.path.exists("setup.py"):
        return "Python (setup.py)"
    elif os.path.exists("pyproject.toml"):
        return "Python (pyproject.toml)"
    elif os.path.exists("requirements.txt"):
        return "Python (requirements.txt)"
    # Add more project type detections as needed
    return "Unknown"

def _read_dependencies() -> Dict[str, Any]:
    """
    Reads dependencies from common dependency files.
    """
    dependencies = {}
    if os.path.exists("requirements.txt"):
        try:
            with open("requirements.txt", "r", encoding="utf-8") as f:
                deps = [line.strip() for line in f if line.strip() and not line.startswith('#')]
                dependencies["requirements.txt"] = deps
        except Exception as e:
            dependencies["requirements.txt_error"] = str(e)
    # Parsing setup.py or pyproject.toml for detailed dependencies is more complex
    # and would require dedicated parsing libraries or logic.
    # For now, we'll just note their presence.
    if os.path.exists("setup.py"):
        dependencies["setup.py_present"] = True
    if os.path.exists("pyproject.toml"):
        dependencies["pyproject.toml_present"] = True
    return dependencies

def _detect_git_repo() -> bool:
    """
    Detects if the current working directory is inside a Git repository.
    """
    # Check for the presence of a .git directory
    return os.path.isdir(".git")

def build_world_state() -> Dict[str, Any]:
    """
    Detects various aspects of the current project and system state.

    This includes:
    - Project type (e.g., Python project via setup.py, requirements.txt)
    - Project dependencies
    - Whether the project is a Git repository
    - The detected Python environment

    Returns:
        A dictionary representing the current system and project state.
    """
    world_state = {
        "project_type": _detect_project_type(),
        "dependencies": _read_dependencies(),
        "is_git_repo": _detect_git_repo(),
        "environment": detect_python_environment()
    }
    return world_state
