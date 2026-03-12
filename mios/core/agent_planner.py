def generate_plan(problem):
    if "ModuleNotFoundError" in problem:
        return [
            "analyze_error",
            "detect_environment",
            "install_dependency",
            "retry_command"
        ]
    else:
        return [
            "analyze_problem"
        ]
