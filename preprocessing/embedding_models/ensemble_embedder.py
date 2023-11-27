from preprocessing.embedding_models.base_embedder import BaseEmbedder
from preprocessing.embedding_models.bert_domain_addapt_embedder import BertAvgDomainAddaptEmbedder
from preprocessing.embedding_models.food2vec_embedder import Food2VecEmbedder
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np


class EnsembleEmbedder(BaseEmbedder):
    def __init__(self, embedders=[BertAvgDomainAddaptEmbedder(), Food2VecEmbedder()]):
        super().__init__()
        self.embedders = embedders
    
    def _embed(self, text: str):
        concatenated_embedding = np.hstack([embedder.embed(text) for embedder in self.embedders])
        return concatenated_embedding

if __name__=="__main__":
    ensemble_embedder = EnsembleEmbedder()
    embed1 = ensemble_embedder.embed("BUTTERMILK PANCAKES BANANA FLAVOUR")
    embed2 = ensemble_embedder.embed("BUTTER WHOLE FAT")
    embed3 = ensemble_embedder.embed("BUTTERMILK")
    embed4 = ensemble_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)