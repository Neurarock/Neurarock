import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("TRIPO3D_API_KEY")
print(f"Loaded API Key: {API_KEY}")

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "type": "text_to_model",
    "prompt": "a small cat"  # Try a simple prompt first
}

response = requests.post("https://api.tripo3d.ai/v2/openapi/task", headers=headers, json=payload)

print("Status:", response.status_code)
print("Response:", response.text)
