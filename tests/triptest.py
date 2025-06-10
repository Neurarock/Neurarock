from dotenv import load_dotenv
import os
import time
import requests

# Load API key from .env
load_dotenv()
APIKEY = os.getenv("TRIPO3D_API_KEY")

if not APIKEY:
    raise ValueError("Missing TRIPO3D_API_KEY in environment.")

# Step 1: Create task
url = "https://api.tripo3d.ai/v2/openapi/task"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {APIKEY}"
}
data = {
    "type": "text_to_model",
    "prompt": "cactus with gun"
}

response = requests.post(url, headers=headers, json=data)

if not response.ok:
    print("❌ Error creating task:", response.status_code, response.text)
    exit(1)

task_id = response.json()["data"]["task_id"]
print(f"✅ Task created with ID: {task_id}")

# Step 2: Poll for result
status_url = f"https://api.tripo3d.ai/v2/openapi/task/{task_id}"
while True:
    status_response = requests.get(status_url, headers=headers)
    status_response.raise_for_status()
    status_data = status_response.json()["data"]

    print(f"⏳ Task status: {status_data['status']}")

    if status_data["status"] == "success":
        result_url = status_data.get("result", {}).get("pbr_model", {}).get("url")

        if not result_url:
            print("⚠️ Could not find 'result.pbr_model.url' in response:")
            print(status_data)
            raise KeyError("Missing model URL in response.")

        print(f"✅ Task complete! Result URL: {result_url}")
        break

    elif status_data["status"] == "failed":
        raise RuntimeError("❌ Task failed.")

    time.sleep(5)

# Step 3: Download model
output_path = "output/a_small_cat.glb"
os.makedirs("output", exist_ok=True)

glb_response = requests.get(result_url)
glb_response.raise_for_status()

with open(output_path, "wb") as f:
    f.write(glb_response.content)

print(f"📦 Model downloaded and saved to: {output_path}")