import json
import os
from pathlib import Path

MEMORY_FILE = Path(__file__).parent / "error_memory.json"

def load_memory() -> dict:
    """Load the error memory from JSON file."""
    try:
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_memory(memory: dict):
    """Save the error memory to JSON file."""
    with open(MEMORY_FILE, 'w') as f:
        json.dump(memory, f, indent=2)

def save_error_solution(error_text: str, solution: str):
    """
    Store a solution for a encountered error.
    
    Args:
        error_text: The error message or key (often the error type and relevant parts)
        solution: The solution that worked for this error
    """
    memory = load_memory()
    memory[error_text] = solution
    save_memory(memory)

def lookup_error_solution(error_text: str) -> str | None:
    """
    Lookup a previously stored solution for an error.
    
    Args:
        error_text: The error message or key to lookup
    
    Returns:
        The stored solution or None if not found
    """
    memory = load_memory()
    return memory.get(error_text)
