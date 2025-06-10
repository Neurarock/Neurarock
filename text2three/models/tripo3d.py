import os
import time
import requests
from dotenv import load_dotenv

load_dotenv()

class Tripo3DModel:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("TRIPO3D_API_KEY")
        if not self.api_key:
            raise ValueError("Missing TRIPO3D_API_KEY in environment.")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        self.api_base = "https://api.tripo3d.ai/v2/openapi"

    def create_task(self, prompt: str) -> str:
        data = {
            "type": "text_to_model",
            "prompt": prompt
        }
        response = requests.post(f"{self.api_base}/task", headers=self.headers, json=data)
        response.raise_for_status()
        task_id = response.json()["data"]["task_id"]
        return task_id

    def poll_task(self, task_id: str, poll_interval=5, timeout=300) -> str:
        status_url = f"{self.api_base}/task/{task_id}"
        start_time = time.time()
        while True:
            response = requests.get(status_url, headers=self.headers)
            response.raise_for_status()
            status_data = response.json()["data"]
            status = status_data["status"]
            print(f"⏳ Task status: {status}")

            if status == "success":
                result_url = status_data.get("result", {}).get("pbr_model", {}).get("url")
                if not result_url:
                    raise KeyError("Missing model URL in response.")
                return result_url
            elif status == "failed":
                raise RuntimeError("Task failed.")

            if time.time() - start_time > timeout:
                raise TimeoutError("Polling timed out.")

            time.sleep(poll_interval)

    def download_model(self, url: str, output_path: str) -> None:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        response = requests.get(url)
        response.raise_for_status()
        with open(output_path, "wb") as f:
            f.write(response.content)
        print(f"📦 Model downloaded and saved to: {output_path}")

    def generate(self, prompt: str, output_path: str = "output/model.glb") -> str:
        task_id = self.create_task(prompt)
        print(f"✅ Task created with ID: {task_id}")

        result_url = self.poll_task(task_id)
        print(f"✅ Task complete! Result URL: {result_url}")

        self.download_model(result_url, output_path)
        return output_path