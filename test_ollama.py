import requests
import json

OLLAMA_API_URL = "http://localhost:11434/api/generate"
OLLAMA_MODEL = "mistral"

print("Testing Ollama connection...")

try:
    response = requests.post(
        OLLAMA_API_URL,
        json={
            "model": OLLAMA_MODEL,
            "prompt": "Hello! This is a test.",
            "stream": False
        },
        timeout=60
    )
    if response.status_code == 200:
        print("SUCCESS: Ollama is running!")
        result = response.json()
        print("Response:", result.get("response", "")[:100])
    else:
        print(f"Error: Status {response.status_code}")
except requests.exceptions.ConnectionError:
    print("ERROR: Could not connect to Ollama")
    print("Make sure to run: C:\\Users\\a2z\\AppData\\Local\\Programs\\Ollama\\ollama.exe serve")
except Exception as e:
    print(f"Error: {e}")
