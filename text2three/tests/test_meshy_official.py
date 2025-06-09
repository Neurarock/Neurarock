import requests
import os
import time

headers = {
  "Authorization": f"Bearer msy_KlDdxxVaV08paGatEOqPYmKX1mDSsAWZ6fYU"
}

# 1. Generate a preview model and get the task ID

generate_preview_request = {
  "mode": "preview",
  "prompt": "a monster mask",
  "negative_prompt": "low quality, low resolution, low poly, ugly",
  "art_style": "realistic",
  "should_remesh": True,
}

generate_preview_response = requests.post(
  "https://api.meshy.ai/openapi/v2/text-to-3d",
  headers=headers,
  json=generate_preview_request,
)

generate_preview_response.raise_for_status()

preview_task_id = generate_preview_response.json()["result"]

print("Preview task created. Task ID:", preview_task_id)