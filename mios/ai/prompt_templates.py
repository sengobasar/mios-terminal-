def explain_command(command):
    return f"""
Explain the following terminal command clearly.

Command:
{command}

Explain:
1. What the command does
2. What each flag means
3. Any risks or warnings
"""

def debug_error(error_text):
    return f"""
Analyze and debug the following error.

Error:
{error_text}

Analyze:
1. Identify the root cause of the error
2. Provide a step-by-step solution to fix the error
3. Explain any potential risks or side effects
"""

def translate_command(command, target_language):
    return f"""
Translate the following terminal command into {target_language}.

Command:
{command}

Translation:
1. Provide the translated command
2. Explain any differences or nuances between the original and translated commands
"""
