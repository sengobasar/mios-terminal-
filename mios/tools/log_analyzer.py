def analyze_log(file_path):
    errors = 0
    warnings = 0
    info = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if "ERROR" in line:
                    errors += 1
                elif "WARNING" in line:
                    warnings += 1
                elif "INFO" in line:
                    info += 1
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

    return {
        "errors": errors,
        "warnings": warnings,
        "info": info
    }
