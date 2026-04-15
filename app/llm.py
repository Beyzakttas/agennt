import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen:4b"


def ask_ollama(prompt: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        return f"Ollama error: {str(e)}"