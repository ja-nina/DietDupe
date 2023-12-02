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
    
def map_indices_to_name(indices: list[int], food: pd.DataFrame, name_colname: str = 'internal'):
    return [food.loc[i, name_colname] for i in indices]

if __name__ == "__main__":
    # read pickle and to txt
    import pickle
    import json
    with open('data/FlavorGraph_node_embedding.pickle', 'rb') as f:
        data = pickle.load(f)
        data_serializable = {k: v.tolist() for k, v in data.items() if isinstance(v, np.ndarray)}
    with open('test.json', 'w') as f:
        json.dump(data_serializable, f)
    
    