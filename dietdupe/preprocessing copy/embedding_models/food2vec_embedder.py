from dietdupe.preprocessing.embedding_models.base_embedder import BaseEmbedder
from food2vec.semantic_nutrition import Estimator
import numpy as np

class Food2VecEmbedder(BaseEmbedder):
    """
    Best embedding model for our use case. Uses the Food2Vec model to embed food items.
    Not optimal since not every ingredient is embedded, but it's the best we have.
    """
    def __init__(self,):
        super().__init__()
        self.model = Estimator()
        
    def _embed(self, text: str) -> np.ndarray:
        try:
            return self.model.embed(text)
        except ValueError:
            return np.zeros(300)