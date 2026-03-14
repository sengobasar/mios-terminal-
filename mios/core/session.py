from pathlib import Path
from typing import List, Dict, Any
import fnmatch

class Session:
    def __init__(self):
        self.current_file: Optional[str] = None
        self.file_history: List[str] = []
        self.project_files: List[str] = []
        self.execution_history: List[Dict[str, Any]] = []

    def update_file_context(self, file_path: str) -> None:
        """Set the current working file."""
        self.current_file = str(Path(file_path).absolute())
        if self.current_file not in self.file_history:
            self.file_history.append(self.current_file)

    def scan_project(self, root_dir: str) -> None:
        """Scan directory for project files."""
        root = Path(root_dir).absolute()
        patterns = ['*.py', '*.md', '*.txt', '*.json']
        
        self.project_files = []
        for pattern in patterns:
            for file in root.rglob(pattern):
                if file.is_file():
                    self.project_files.append(str(file))
