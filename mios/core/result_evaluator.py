def evaluate_result(step, result):
    if "error" in result.lower():
        return {"success": False}
    else:
        return {"success": True}
