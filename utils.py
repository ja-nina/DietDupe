import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity

def plot_histogram(df, column, name_of_embedder):
    plt.hist(df[column].fillna(0), bins=10, edgecolor='black')
    plt.title(f'Histogram of Similarity with {name_of_embedder} embeddings')
    plt.xlabel('Similarity')
    plt.ylabel('Frequency')
    plt.show()


def masked_cosine_similarity(embedding1, embedding2):
    """
    Utility function for EnsembleEmbedder - Food2Vec embedder can return all 0s as embeddings
    therefore we need to mask them out before calculating cosine similarity on the concatenated 
    embedding
    """
    embedding1 = np.array(embedding1).astype(np.float32)
    embedding2 = np.array(embedding2).astype(np.float32)
    
    mask1 = embedding1 == 0.0
    mask2 = embedding2 == 0.0
    
    embed1_to_subtract = (mask2 @ (embedding1.T ** 2)).T
    embed2_to_subtract = mask1 @ (embedding2.T ** 2)
    
    norm1 = np.linalg.norm(embedding1, axis=1)
    norm2 = np.linalg.norm(embedding2, axis=1)
    
    to_subtract_from1 =  np.tile(norm1, (len(norm2), 1)).T
    to_subtract_from2 =  np.tile(norm2, (len(norm1), 1))
    
    masked_outer = np.sqrt(to_subtract_from1**2 -embed1_to_subtract) * np.sqrt(to_subtract_from2**2-embed2_to_subtract)
    dot_product = np.dot(embedding1, embedding2.T)
    return dot_product / masked_outer
    
def map_indices_to_colname(indices: list[int], food: pd.DataFrame, name_colname: str = 'internal'):
    return [food.loc[i, name_colname] for i in indices]

def map_indices_and_filter_by_colname(base_index: str, indices: list[int], food: pd.DataFrame, higher: list[str], lower: list[str]):
    valid_indices = indices
    for column in higher:
        valid_indices = [i for i in valid_indices if food.loc[i, column] >= food.loc[base_index, column]]
    for column in lower:
        valid_indices = [i for i in valid_indices if food.loc[i, column] <= food.loc[base_index, column]]

    return valid_indices

def input_ingredients():
    ingredients = []
    while True:
        ingredient = input("Enter ingredient index or 'q' to quit: ")
        if ingredient == 'q':
            break
        else:
            ingredients.append(int(ingredient))
    return ingredients
    
