def classify_intent(text: str):
    """
    Detect the intent of a user command.
    """

    text = text.lower()

    # compress folder intent
    if "compress" in text or "zip" in text or "archive" in text:
        return {"intent": "compress_folder"}

    # find large files intent
    if "find large files" in text or "files larger than" in text or "large files" in text:
        return {"intent": "find_large_files"}

    # explain command intent
    if text.startswith("explain") or "explain command" in text:
        return {"intent": "explain_command"}

    return {"intent": "unknown"}