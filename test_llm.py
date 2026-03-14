from mios.ai.llm_client import get_llm_response

prompt = """
You are an AI assistant that helps users with technical tasks.
Always respond with a JSON object representing the action to take.

Rules for Action Selection:
1. If the user asks to "open", "read", "show", or "view" a file, the action MUST be "read_file". DO NOT use "create_file" for this.
2. If the user asks to "create", "make", or "write" a new file, the action is "create_file".
3. If the user asks to "install", the action is "install_package".

Allowed actions:
create_file, modify_file, read_file, run_command, install_package

Format examples:
{
    "action": "create_file",
    "file": "filename",
    "content": "file content"
}

{
    "action": "read_file",
    "file": "filename"
}
"""

res = get_llm_response(prompt, "open test.txt")
print("LLM raw response:")
print(repr(res))
