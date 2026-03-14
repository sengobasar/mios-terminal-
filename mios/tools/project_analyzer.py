import os
import ast

def analyze_project(root_path="."):
    """
    Analyzes a project to find all .py files and detect imports within them.

    Args:
        root_path (str): The root directory of the project to analyze. Defaults to ".".

    Returns:
        dict: A dictionary containing:
            - "python_files" (list): A list of paths to all .py files found.
            - "imports" (dict): A dictionary where keys are file paths and values
                                are lists of imported module names from that file.
    """
    python_files = []
    imports = {}

    for dirpath, _, filenames in os.walk(root_path):
        for filename in filenames:
            if filename.endswith(".py"):
                file_path = os.path.join(dirpath, filename)
                python_files.append(file_path)
                
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        tree = ast.parse(f.read(), filename=file_path)
                        
                    file_imports = []
                    for node in ast.walk(tree):
                        if isinstance(node, ast.Import):
                            for alias in node.names:
                                file_imports.append(alias.name)
                        elif isinstance(node, ast.ImportFrom):
                            # Handle relative imports by checking module attribute
                            if node.module:
                                file_imports.append(node.module)
                    
                    imports[file_path] = file_imports
                except Exception as e:
                    print(f"Error parsing file {file_path}: {e}")
                    imports[file_path] = [] # Assign empty list on error

    return {
        "python_files": python_files,
        "imports": imports
    }
