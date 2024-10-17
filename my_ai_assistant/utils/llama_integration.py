import requests

def get_llama_response(prompt):
    url = "http://localhost:11434/completion"  # Assuming Ollama runs locally
    payload = {
        "model": "llama-3.2",
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(url, json=payload)
    return response.json().get("text", "")
