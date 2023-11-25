from abc import ABC, abstractmethod
import numpy as np

class BaseEmbedder(ABC):
    def __init__(self):
        self.cache = {}
        
    @abstractmethod
    def _embed(self, text: str) -> np.ndarray:
        pass
    
    def embed(self, text: str) -> np.ndarray:
        return self.cache.get(text, self.embed_and_cache(text))
    
    def embed_and_cache(self, text: str) -> np.ndarray:
        self.cache[text] = self._embed(text)
        return self.cache[text]