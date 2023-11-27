import matplotlib.pyplot as plt

def plot_histogram(df, column, name_of_embedder):
    plt.hist(df[column].fillna(0), bins=10, edgecolor='black')
    plt.title(f'Histogram of Similarity with {name_of_embedder} embeddings')
    plt.xlabel('Similarity')
    plt.ylabel('Frequency')
    plt.show()