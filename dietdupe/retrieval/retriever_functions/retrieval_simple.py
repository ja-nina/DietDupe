from sklearn.metrics.pairwise import euclidean_distances # euclidian distances because we work on tsne projections
from dietdupe.utils import map_indices_to_colname, map_indices_and_filter_by_colname
import numpy as np

def retrieval_simple(foods, food_embeddings, recipe_indices,  top_k, *args):
    food_embeddings_array = list(food_embeddings.values())
    node_id_tosequential = {seq_id: node_id for seq_id, node_id in enumerate(list(food_embeddings.keys()))}
    subset_embeddings = [food_embeddings[index] for index in recipe_indices]
    similarity_matrix = euclidean_distances(subset_embeddings, food_embeddings_array)
    most_similar_foods = np.argsort(similarity_matrix, axis=1)[:, :top_k]
    named_foods = [map_indices_to_colname([node_id_tosequential[index] for index in indices], foods) for indices in most_similar_foods]
    return named_foods
