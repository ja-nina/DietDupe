from abc import ABC, abstractmethod
import numpy as np
import torch

class BaseEmbedder(ABC):
    def __init__(self):
        self.model = None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.cache = {}
        
    def post_init(self):
        self.model.to(self.device)

    @abstractmethod
    def _embed(self, text: str) -> np.ndarray:
        pass
    
    def embed(self, text: str) -> np.ndarray:
        return self.cache.get(text, self.embed_and_cache(text))
    
    def embed_and_cache(self, text: str) -> np.ndarray:
        self.cache[text] = self._embed(text)
        return self.cache[text]