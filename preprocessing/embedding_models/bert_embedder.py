from preprocessing.embedding_models.base_embedder import BaseEmbedder
from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class BertEmbedder(BaseEmbedder):
    def __init__(self):
        self.model = BertModel.from_pretrained('bert-base-uncased')
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        

    
    def embed(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs, output_hidden_states=True)
        return outputs.hidden_states[-1].detach().numpy()[0, 0, :].flatten()
    
    
class BertEmbedderAvg(BertEmbedder):
    def __init__(self):
        super().__init__()
    
    def embed(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs)
        return outputs[0].detach().numpy().squeeze().mean(axis=0)
    
if __name__=="__main__":
    bert_embedder = BertEmbedder()
    embed1 = bert_embedder.embed("BUTTERMILK PANCAKES")
    embed2 = bert_embedder.embed("BUTTER WHOLE FAT")
    embed3 = bert_embedder.embed("BUTTERMILK")
    embed4 = bert_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)
    
    embed1 = bert_embedder.embed_avg("BUTTERMILK PANCAKES")
    embed2 = bert_embedder.embed_avg("BUTTER WHOLE FAT")
    embed3 = bert_embedder.embed_avg("BUTTERMILK")
    embed4 = bert_embedder.embed_avg("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)

    

