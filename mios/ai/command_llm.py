from typing import Dict, Any
import json
from mios.ai.llm_client import get_llm_response

def extract_json(text: str):
    """
    Extract the first valid JSON object from a text response.
    """
    import re, json
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        return None
    try:
        return json.loads(match.group())
    except Exception:
        return None


def interpret_with_llm(command: str) -> Dict[str, Any]:
    """
    Uses LLM to interpret a user command and return a structured action.
    
    Args:
        command: The user's natural language command
        
    Returns:
        A dictionary with structured action details (e.g., create_file, run_command)
    """
    # System prompt to guide the LLM's response format
    system_prompt = """
    You are an AI assistant that helps users with technical tasks.
    Always respond with a JSON object representing the action to take.
    
    Rules for Action Selection:
    1. If the user asks to "open", "read", "show", or "view" a file, the action MUST be "read_file". DO NOT use "create_file" for this.
    2. If the user asks to "create", "make", or "write" a new file, the action is "create_file".
    3. If the user asks to "install", the action is "install_package".
    
    Allowed actions:
    create_file, modify_file, read_file, run_command, install_package
    
    Format examples:
    {
        "action": "create_file",
        "file": "filename",
        "content": "file content"
    }
    
    {
        "action": "read_file",
        "file": "filename"
    }
    """
    
    for attempt in range(2):
        # Get LLM response using the existing client
        llm_response = get_llm_response(
            system_prompt=system_prompt,
            user_prompt=command if attempt == 0 else "Return ONLY valid JSON."
        )
        
        data = extract_json(llm_response)
        
        if data is not None:
            return data
            
    # Default fallback if parsing fails twice        
    return {"action": "unknown"}
