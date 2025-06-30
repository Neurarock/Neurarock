import requests
import json
import os
from dotenv import load_dotenv
import time
from pathlib import Path
from text2three.base import BaseModel

class ModelslabModel(BaseModel):
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("MODELSLAB_API_KEY")
        if not self.api_key:
            raise ValueError("MODELSLAB_API_KEY not found in environment variables.")

        self.url = "https://modelslab.com/api/v6/3d/text_to_3d"

        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)

    def generate(self, prompt: str, output_path: Path = None, negative_prompt: str = "", **kwargs) -> Path:
        headers = {
            "Content-Type": "application/json"
        }
        payload = json.dumps({
            "key": self.api_key,
            "foreground_ratio": "0.85",
            "prompt": prompt,
            "num_inference_steps": "30",
            "resolution": 512,
            "guidance_scale": "3",
            "ss_sampling_steps": 50,
            "slat_sampling_steps": 50,
            "seed": 0,
            "temp": "no",
            "webhook": None,
            "track_id": None
        })


        print(f"[INFO] Submitting prompt to Modelslab: {prompt}")
        response = requests.request("POST", self.url, headers=headers, data=payload)
        data = response.json()
        print("[DEBUG] Full response:", data)
        

        status = data.get("status")
        print("Status:", status)

        if status == "success":
            model_url = data.get("output")[0]
        
        elif status == "processing":
            model_url = data.get("future_links")[0]
        
        else:
            raise RuntimeError("Generation status error")

        # Prepare output path
        if not output_path:
            file_name = f"{uuid}.obj"
            output_path = self.output_dir / file_name

        # HTTPS status check for 120s

        print(f"[INFO] Waiting for URL to be reachable: {model_url}")
        start_time = time.time()
        timeout = 120
        interval = 1

        while True:
            try:
                response = requests.head(model_url)
                status_code = response.status_code
                elapsed = int(time.time() - start_time)
                print(f"\r[INFO] Time elapsed: {elapsed}s, Status code: {status_code}", end="")

                if status_code == 200:
                    print("\n[INFO] URL is reachable. Starting download...")
                    break  # Exit the loop to download

                if elapsed > timeout:
                    raise RuntimeError(f"URL unreachable after {timeout} seconds, last status code: {status_code}")

            except requests.RequestException as e:
                elapsed = int(time.time() - start_time)
                print(f"\r[INFO] Time elapsed: {elapsed}s, Exception: {e}", end="")
                if elapsed > timeout:
                    raise RuntimeError(f"URL unreachable after {timeout} seconds, exception: {e}")

            time.sleep(interval)
       

        # Download the model
        print(f"[INFO] Downloading model from {model_url}")
        with requests.get(model_url, stream=True) as r:
            r.raise_for_status()
            with open(output_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        print(f"[INFO] Model saved to {output_path}")
        return output_path