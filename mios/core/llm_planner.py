import json
from typing import Dict, List, Any
from mios.ai.llm_client import get_llm_response
from mios.core.context_builder import build_context

SYSTEM_PROMPT = """You are an expert debugging assistant. Analyze the error and generate a multi-step repair plan.

Guidelines:
1. Return ONLY valid JSON with the exact schema specified
2. Carefully inspect the error message and file content
3. Generate actionable steps to fix the error
4. Prioritize edits to existing code first
5. Include package installation if imports are missing
6. End with "retry_command" to test the fix

Respond with this JSON structure:
{
 "plan": [
   {"action": "read/edit/install/run", "details": "..."},
   ...
 ]
}
"""

def validate_plan(plan_data: Dict) -> bool:
    """Validate the LLM-generated plan structure."""
    if not isinstance(plan_data, dict):
        return False
    if "plan" not in plan_data:
        return False
    if not isinstance(plan_data["plan"], list):
        return False
    required_keys = {"action"}
    for step in plan_data["plan"]:
        if not all(key in step for key in required_keys):
            return False
    return True

def generate_llm_plan(error: str, file_path: str = None) -> List[Dict[str, Any]]:
    """
    Generate a repair plan using LLM analysis.
    
    Args:
        error: Error message to analyze
        file_path: Optional file path related to the error
        
    Returns:
        List of action steps to take
    """
    context = build_context(error, file_path)
    
    user_prompt = f"""
Error:
{context['error']}

File Content:
{context.get('file_content', '')}

Project Files:
{context.get('project_files', [])}
"""
    try:
        response = get_llm_response(SYSTEM_PROMPT, user_prompt)
        plan_data = json.loads(response)
        
        if not validate_plan(plan_data):
            raise ValueError("Invalid plan structure")
            
        return plan_data["plan"]
    
    except (json.JSONDecodeError, ValueError) as e:
        return [{"action": "analyze_problem", "error": str(e)}]
