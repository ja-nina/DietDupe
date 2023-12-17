import numpy as np
import pandas as pd
from typing import Dict, Tuple
from dietdupe.retrieval.utils import parse_args
from sklearn.metrics.pairwise import euclidean_distances
from dietdupe.utils import map_indices_to_colname, map_indices_and_filter_by_colname # TODO: move to retriever utils

p = 0.1 # parameter - move to retriever class
def retrieval_with_restrictions_simple_context(foods: pd.DataFrame, food_embeddings: Dict[int, np.ndarray], recipe_indices: list[int],  top_k: int, restrictions: list[Tuple[str, str]] = [])-> list[list[str]]:
    lower, higher = parse_args(restrictions)
    
    food_embeddings_array = list(food_embeddings.values())
    node_id_to_sequential = {seq_id: node_id for seq_id, node_id in enumerate(list(food_embeddings.keys()))}
    subset_embeddings = [food_embeddings[index] for index in recipe_indices]
    
    # sum_embeddings = np.sum(subset_embeddings)
    # subset_embeddings = [embedding - sum_embeddings*p for embedding in subset_embeddings]
    
    similarity_matrix = euclidean_distances(subset_embeddings, food_embeddings_array)
    most_similar_foods = np.argsort(similarity_matrix, axis=1)[:, :]
    
    most_similar_filtered = []
    for dietdupes in most_similar_foods:
        base_index= node_id_to_sequential[dietdupes[0]]
        dietdupes_node_ids = [node_id_to_sequential[index] for index in dietdupes]
        filtered_indices = map_indices_and_filter_by_colname(base_index,  dietdupes_node_ids, foods, higher, lower)[:top_k]
        most_similar_filtered.append(filtered_indices)

    named_foods = [map_indices_to_colname([index for index in indices], foods, ) for indices in most_similar_filtered]
    return named_foods