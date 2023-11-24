from abc import ABC, abstractmethod
import numpy as np

class BaseEmbedder(ABC):
    @abstractmethod
    def embed(self, text: str) -> np.ndarray:
        pass