from preprocessing.embedding_models.base_embedder import BaseEmbedder
from preprocessing.embedding_models.bert_embedder import BertEmbedder
from sklearn.metrics.pairwise import cosine_similarity

import numpy as np
import pandas as pd

class Matcher:
    def __init__(self, model_for_embedding, data_internal, data_external):
        self.data_internal = data_internal
        self.data_external = data_external
        self.model_for_embedding = model_for_embedding
        
        self.hierarchical_dict = {}
        self.embedded_hierarchical_dict = {}
        self.similarity_matrix = None
        self.df_results = None
        
        self._create_emmpty_df()
    
    def _create_emmpty_df(self):
        self.df_results = pd.DataFrame()
        self.df_results['internal'] = self.data_internal
        
    def hierarchy_stripper(self, hierarchical_text: list[str]):
        for i in range(1, len(hierarchical_text)+1):
            yield " ".join(hierarchical_text[:i])

    def _create_hierarchical_list(self):
        external_list_splitted = [[x.strip() for x in name.split(",")] for name in self.data_external]
        self.hierarchical_dict = dict([(" ".join(name), list(self.hierarchy_stripper(name))) for name in external_list_splitted])
        return self.hierarchical_dict
    
    def _embed_hierarchical_dict(self):
        self.embedded_hierarchical_dict = dict([(name, list(self.model_for_embedding.embed(name))) for name in self.hierarchical_dict])
        return self.embedded_hierarchical_dict
    
    def _prepare_extrenal_data_hierarchical(self):
        self._create_hierarchical_list()
        keywords = [key for key, words in self.hierarchical_dict.items() for _ in words]
        hierarchy_words = [word for _, words in self.hierarchical_dict.items() for word in words]
        embeddings = np.array([self.model_for_embedding.embed(word) for word in hierarchy_words])
        print(keywords, hierarchy_words)
        return keywords, hierarchy_words, embeddings
    
    def _match_data(self, embeddings_internal, embeddings_external, keywords_external, hierarchial_words_external):
        similarity_matrix = cosine_similarity(embeddings_internal, embeddings_external)
        
        most_similar_indices = np.argmax(similarity_matrix, axis=1)
        most_similar_values = np.max(similarity_matrix, axis=1)

        most_similar = list(zip(range(len(self.data_internal)), most_similar_indices, most_similar_values))
        
        self.df_results['best_match'] = None
        self.df_results['similarity_of_best_match'] = None

        for i, j, sim in most_similar:
            self.df_results.loc[i, 'exact_best_match'] = hierarchial_words_external[j]
            self.df_results.loc[i, 'best_match'] = keywords_external[j]
            self.df_results.loc[i, 'similarity'] = sim
            
        return self.df_results

        
    def run(self):
        embeddings_internal = np.array([self.model_for_embedding.embed(word) for word in self.data_internal])
        keywords, hierarchy_words, embeddings_external = self._prepare_extrenal_data_hierarchical()
        
        return self._match_data(embeddings_internal, embeddings_external, keywords, hierarchy_words)
    
if __name__=="__main__":
    # Test
    model = BertEmbedder()
    internal_data = ["lowfat milk", "juice orange", "bananas"]
    external_data = ["MILK, LOWFAT, 2%", "MILK, BANANA FLAVOUR, FULL FAT", "JUICE, ORANGE, CHILLED, INCLUDES FROM CONCENTRATE, WITH ADDED CALCIUM AND VITAMIN D"]
    matcher = Matcher(model, internal_data, external_data)
    res = matcher.run()
    print(res)
    
    