from pathlib import Path
from typing import Dict, Optional
from mios.core.session import Session

def build_context(error: str, file_path: Optional[str] = None) -> Dict[str, any]:
    """
    Builds a context dictionary containing:
    - The error message
    - Content of the current file (if provided)
    - List of project files
    
    Args:
        error: The error message to include in context
        file_path: Optional path to the file being worked on
    
    Returns:
        Dictionary containing error, file_content, and project_files
    """
    session = Session()
    context = {
        "error": error,
        "file_content": "",
        "project_files": []
    }
    
    if file_path:
        try:
            context["file_content"] = Path(file_path).read_text(encoding="utf-8")
            session.update_file_context(file_path)
        except Exception as e:
            context["file_content"] = f"Error reading file: {str(e)}"
    
    if session.project_files:
        context["project_files"] = session.project_files
    else:
        # If no project files scanned yet, scan current directory
        session.scan_project(".")
        context["project_files"] = session.project_files
    
    return context
