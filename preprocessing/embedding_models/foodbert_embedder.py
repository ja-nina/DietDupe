#!/usr/bin/env python3
import sys
sys.path.append("../../")
from foodbert.food_extractor.food_model import FoodModel
from preprocessing.embedding_models.base_embedder import BaseEmbedder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class FoodBertEmbedder(BaseEmbedder):
    """
    FoodBERT: Food Extraction with DistilBERT
    <https://github.com/chambliss/foodbert>
    """
    def __init__(self,):
        super().__init__()
        self.model = FoodModel("chambliss/distilbert-for-food-extraction")

    def _embed(self, text: str) -> np.ndarray:
        try:
            inputs = self.model.tokenizer(
                text,
                padding=True,
                truncation=True,
                add_special_tokens=False,
                return_tensors="pt",
            ).to(self.device)
            outputs = self.model.model.forward(inputs["input_ids"], output_hidden_states=True)
            return outputs.hidden_states[-1].detach().cpu().numpy()[0, 0, :].flatten()
        except ValueError:
            return np.zeros(300)


if __name__ == "__main__":
    foodbert_embedder = FoodBertEmbedder()
    embed1 = foodbert_embedder.embed("BUTTERMILK PANCAKES BANANA FLAVOUR")
    embed2 = foodbert_embedder.embed("BUTTER WHOLE FAT")
    embed3 = foodbert_embedder.embed("BUTTERMILK")
    embed4 = foodbert_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)
