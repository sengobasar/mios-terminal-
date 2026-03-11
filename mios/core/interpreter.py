def interpret_intent(intent, user_input):
    if intent == "compress_folder":
        return {"command": "tar -czf archive.tar.gz folder"}
    elif intent == "find_large_files":
        return {"command": "find . -size +1G"}
    elif intent == "explain_command":
        return {"action": "explain_command"}
    else:
        return {"error": "Unknown intent"}
