from typing import Dict, Any
import json
from mios.llm.llm_client import get_llm_response

def interpret_with_llm(command: str) -> Dict[str, Any]:
    """
    Uses LLM to interpret a user command and return a structured action.
    
    Args:
        command: The user's natural language command
        
    Returns:
        A dictionary with structured action details (e.g., create_file, run_command)
        
    Raises:
        ValueError: If LLM response cannot be parsed as valid JSON
    """
    # System prompt to guide the LLM's response format
    system_prompt = """
    You are an AI assistant that helps users with technical tasks.
    Always respond with a JSON object representing the action to take.
    
    Common action types:
    - create_file: Creates a new file
    - modify_file: Edits an existing file 
    - run_command: Executes a system command
    - install_package: Installs a package/module
    
    Example responses:
    {
        "action": "create_file",
        "file": "hello.py",
        "content": "print('hello world')"
    }
    
    {
        "action": "run_command",
        "command": "pip install numpy",
        "description": "Installs NumPy package"
    }
    """
    
    # Get LLM response using the existing client
    llm_response = get_llm_response(
        system_prompt=system_prompt,
        user_prompt=command
    )
    
    try:
        # Attempt to parse the LLM's response as JSON
        response_json = json.loads(llm_response.strip())
        return response_json
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse LLM response as JSON: {e}\nResponse was: {llm_response}")
