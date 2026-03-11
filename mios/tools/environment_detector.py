import os
import toml

def detect_python_environment():
    if "VIRTUAL_ENV" in os.environ:
        return {"environment": "venv"}
    elif "CONDA_PREFIX" in os.environ:
        return {"environment": "conda"}
    elif os.path.exists("pyproject.toml"):
        with open("pyproject.toml", "r") as file:
            pyproject = toml.load(file)
            if "tool" in pyproject and "poetry" in pyproject["tool"]:
                return {"environment": "poetry"}
    return {"environment": "default"}
