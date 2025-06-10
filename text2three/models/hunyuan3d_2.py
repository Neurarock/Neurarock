import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("SYNEXA_API_KEY")
if not api_key:
    raise ValueError("SYNEXA_API_KEY not found in environment variables.")

print("API KEY:", api_key)

import synexa
output = synexa.run(
    "tencent/hunyuan3d-2",
    input={
        "seed": 1234,
        "image": "",
        "steps": 5,
        "caption": "Cactus",
        "shape_only": True,
        "guidance_scale": 5.5,
        "multiple_views": [],
        "check_box_rembg": True,
        "octree_resolution": "256"
    }
)

print(output)