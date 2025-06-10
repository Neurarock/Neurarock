from gradio_client import Client
from pathlib import Path
import base64
import os
import shutil
from dotenv import load_dotenv

class ShapeEModel:
    def __init__(self):
        self.client = Client("hysts/Shap-E")


    def generate(self, prompt: str, output_path: Path = None, **kwargs) -> Path:
        if output_path is None:
            output_dir = Path(__file__).parent.parent / "output"
            output_dir.mkdir(parents=True, exist_ok=True)
            output_path = output_dir / f"{prompt.replace(' ', '_')}.glb"

        # Call Shape-E API
        result = self.client.predict(
            prompt=prompt,
            seed=0,
            guidance_scale=15,
            num_inference_steps=64,
            api_name="/text-to-3d",
            **kwargs
        )

        shutil.copy(result, output_path)

        print("Shape-E model saved to:", output_path)
        return output_path
