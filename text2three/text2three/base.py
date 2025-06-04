from abc import ABC, abstractmethod
from pathlib import Path

class BaseModel(ABC):
    @abstractmethod
    def generate(self, prompt: str, **kwargs) -> Path:
        """Generate a 3D model from a text prompt."""
        pass
