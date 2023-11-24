from preprocessing.embedding_models.base_embedder import BaseEmbedder
from food2vec.semantic_nutrition import Estimator
import numpy as np

class Food2VecEmbedder(BaseEmbedder):
    """
    Best embedding model for our use case. Uses the Food2Vec model to embed food items.
    Not optimal since not every ingredient is embedded, but it's the best we have.
    """
    def __init__(self, embeddings_dict: dict[str, list[float]]):
        self.estimator = Estimator() 
        self.embeddings_dict = embeddings_dict
        
    def embed(self, text: str) -> np.ndarray:
        return self.estimator.embed(text)