import requests

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
