import os
import time
import requests
from pathlib import Path
from text2three.base import BaseModel
from dotenv import load_dotenv


class MeshyModel(BaseModel):
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MESHY_API_KEY_DEV")
        if not self.api_key:
            raise ValueError("MESHY_API_KEY not found in environment variables.")
        self.base_url = "https://api.meshy.ai/openapi/v2/text-to-3d"
        print("API KEY:", self.api_key)

    def generate(self, prompt: str, output_path: Path = None, **kwargs) -> Path:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "mode": "preview",
            "prompt": prompt
        }

        # Initiate the generation task
        response = requests.post(self.base_url, headers=headers, json=payload)
        response.raise_for_status()
        task_id = response.json().get("result")

        # Poll for task completion
        status_url = f"{self.base_url}/{task_id}"
        while True:
            status_response = requests.get(status_url, headers=headers)
            status_response.raise_for_status()
            status_data = status_response.json()
            if status_data.get("status") == "SUCCEEDED":
                print("Task finished.")
                break
            elif status_data.get("status") == "FAILED":
                raise RuntimeError("Meshy model generation failed.")
            print("Task Status:", status_data.get("status"),"| Progress:", status_data.get("progress"), "| Retrying in 5 seconds...")  
            # Wait before polling again
            time.sleep(5)

        # Download the generated model
        model_url = status_data["model_urls"]["glb"]
        if not model_url:
            raise ValueError("Model URL not found in the response.")

        if not output_path:
            output_path = Path(f"{prompt.replace(' ', '_')}.glb")

        with requests.get(model_url, stream=True) as r:
            r.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print("Preview model downloaded.")
        return output_path


