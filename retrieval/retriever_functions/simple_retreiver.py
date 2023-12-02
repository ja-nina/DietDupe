# distance based on similarity only 
from sklearn.metrics.pairwise import euclidean_distances # euclidian distances because we work on tsne projections
from utils import map_indices_to_name
import numpy as np

def simple_similarity_distance(foods, food_embeddings, recipe_indices,  top_k, args = None):
    food_embeddings_array = [food for food in food_embeddings.values()]
    node_id_tosequential = dict([(seq_id, node_id) for seq_id, node_id in enumerate(list(food_embeddings.keys()))])
    subset_embeddings = [food_embeddings[index_ingrd] for index_ingrd in recipe_indices]
    similarity_matrix = euclidean_distances(subset_embeddings, food_embeddings_array)
    sorted_indices = np.argsort(similarity_matrix, axis=1)
    most_similar_foods = sorted_indices[:, :top_k]
    named_foods = [map_indices_to_name([node_id_tosequential[dupe] for dupe in dupes], foods) for dupes in most_similar_foods]
    return named_foods
    
    