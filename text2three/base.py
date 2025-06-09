from pathlib import Path
from abc import ABC, abstractmethod


class BaseModel(ABC):
    """
    Abstract base class for text-to-3D model generation backends.
    All implementations (e.g., Meshy, Shap-E, Point-E) should inherit from this.
    """

    @abstractmethod
    def generate(self, prompt: str, output_path: Path = None, **kwargs) -> Path:
        """
        Generate a 3D model from a text prompt.
        
        Args:
            prompt (str): Text prompt to generate the 3D model.
            output_path (Path, optional): Path to save the generated model. Defaults to prompt.glb.

        Returns:
            Path: Path to the saved .glb file.
        """
        pass
