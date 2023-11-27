from transformers import AutoModelForMaskedLM, AutoModel
from transformers import AutoTokenizer
from preprocessing.embedding_models.base_embedder import BaseEmbedder
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class BertDomainAddaptEmbedder(BaseEmbedder):
    def __init__(self):
        super().__init__()
        self.model = AutoModel.from_pretrained("ja-nina/bert-base-uncased-dietdupe-foodb-desc")
        self.tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    
    def _embed(self, text):
        inputs = self.tokenizer(text, return_tensors='pt', truncation=True, padding=True)
        outputs = self.model(**inputs)
        sentence_embedding = outputs.last_hidden_state[0, 0, :]  # Embedding of the whole text
        return sentence_embedding.detach().numpy()

class BertAvgDomainAddaptEmbedder(BertDomainAddaptEmbedder):
    def __init__(self):
        super().__init__()
    
    def _embed(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs)
        return outputs[0].detach().numpy().squeeze().mean(axis=0)

if __name__=="__main__":
    bert_embedder = BertDomainAddaptEmbedder()
    embed1 = bert_embedder.embed("BUTTERMILK PANCAKES")
    embed2 = bert_embedder.embed("BUTTER WHOLE FAT")
    embed3 = bert_embedder.embed("BUTTERMILK")
    embed4 = bert_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)
    
    bert_embedder = BertAvgDomainAddaptEmbedder()
    embed1 = bert_embedder.embed("BUTTERMILK PANCAKES")
    embed2 = bert_embedder.embed("BUTTER WHOLE FAT")
    embed3 = bert_embedder.embed("BUTTERMILK")
    embed4 = bert_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)