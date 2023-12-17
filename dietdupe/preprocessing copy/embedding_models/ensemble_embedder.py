from dietdupe.preprocessing.embedding_models.base_embedder import BaseEmbedder
from dietdupe.preprocessing.embedding_models.bert_domain_addapt_embedder import BertAvgDomainAddaptEmbedder
from dietdupe.preprocessing.embedding_models.food2vec_embedder import Food2VecEmbedder
from utils import masked_cosine_similarity

import numpy as np


class EnsembleEmbedder(BaseEmbedder):
    def __init__(self, embedders=[BertAvgDomainAddaptEmbedder(), Food2VecEmbedder(), Food2VecEmbedder()]):
        super().__init__()
        self.embedders = embedders
    
    def _embed(self, text: str):
        concatenated_embedding = np.hstack([embedder.embed(text) for embedder in self.embedders])
        return concatenated_embedding

if __name__=="__main__":
    ensemble_embedder = EnsembleEmbedder()
    embed1 = ensemble_embedder.embed("100%% bran")
    embed2 = ensemble_embedder.embed("oat bran")
    embed3 = ensemble_embedder.embed("mixed nuts")
    similarity_matrix = masked_cosine_similarity([embed1, embed2, embed3], [embed1, embed2, embed3])
    print(similarity_matrix)