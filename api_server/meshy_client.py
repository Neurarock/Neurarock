import os
import requests
import time

MESHY_API_KEY = os.getenv("MESHY_API_KEY")

async def generate_meshy_3d(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {MESHY_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {"mode": "preview", "prompt": prompt}
    response = requests.post("https://api.meshy.ai/openapi/v2/text-to-3d", headers=headers, json=payload)
    response.raise_for_status()
    task_id = response.json()["result"]

    status_url = f"https://api.meshy.ai/openapi/v2/text-to-3d/{task_id}"

    while True:
        r = requests.get(status_url, headers=headers)
        r.raise_for_status()
        status = r.json()
        if status["status"] == "succeeded":
            return status["result"]["model_url"]
        elif status["status"] == "failed":
            raise Exception("Meshy generation failed")
        time.sleep(5)
