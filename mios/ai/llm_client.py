import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

MODEL_NAME = "deepseek-coder:1.3b"   # you can change to mistral or qwen later



def get_llm_response(system_prompt: str, user_prompt: str) -> str:
    """
    Sends a prompt to the local Ollama model and returns the response text.
    """

    prompt = f"""
{system_prompt}

User request:
{user_prompt}

Respond ONLY with valid JSON.
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()

        result = response.json()

        return result.get("response", "").strip()

    except Exception as e:
        return f'{{\\"action\\":\\"error\\",\\"message\\":\\"{str(e)}\\"}}'
def explain_command(command):
    prompt = f"Please explain the following command: {command}"
    url = "https://api.ollama.com/explain"  # Replace with the actual API endpoint
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer YOUR_API_KEY"  # Replace with your actual API key
    }
    data = {
        "prompt": prompt
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        explanation = response.json().get("explanation", "No explanation available")
        return {"explanation": explanation}
    except requests.exceptions.RequestException as e:
        return {"explanation": f"Error explaining command: {e}"}
