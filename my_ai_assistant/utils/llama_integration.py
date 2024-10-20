import requests

def get_llama_response(prompt):
    url = "http://localhost:11434"  # Assuming Ollama runs locally
    payload = {
        "model": "llama3.2",
        "prompt": prompt,
        "max_tokens": 150
    }

    response = requests.post(url, json=payload)
    
    # Check if the response is JSON
    if response.headers.get('Content-Type') == 'application/json':
        try:
            data = response.json()
            return data.get("text", "")
        except ValueError:
            print("Invalid JSON response")
            print(response.text)
    else:
        print(f"Received non-JSON response: {response.text}")
        return "Sorry, something went wrong."
