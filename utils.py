import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity, check_pairwise_arrays

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
    embedding1 = np.array(embedding1)
    embedding2 = np.array(embedding2)
    
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
    

if __name__=="__main__":
    
    embeddings1 = np.array([
        np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
        np.array([0.0, 0.0, 5.0, 1.0, 1.0]),
    ])

    embeddings2 = np.array([
        np.array([1.0, 2.0, 3.0, 4.0, 5.0]),
        np.array([0.0, 0.0, 3.0, 4.0, 5.0]),
        np.array([0.0, 0.0, 5.0, 1.0, 1.0]),
        np.array([3.0, 9.0, 5.0, 1.0, 1.0])
    ])

    cos_sim_masked = masked_cosine_similarity(embeddings1, embeddings2)
    print("Cosine Similarities Masked:\n", cos_sim_masked)
    
    regular_cosine_sim = cosine_similarity(embeddings1, embeddings2)
    print("Regular Cosine Similarities:\n", regular_cosine_sim )