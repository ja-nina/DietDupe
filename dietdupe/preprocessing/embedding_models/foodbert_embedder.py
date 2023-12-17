from dietdupe.preprocessing.embedding_models.base_embedder import BaseEmbedder
from transformers import BertModel, BertTokenizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class FoodBertEmbedder(BaseEmbedder):
    def __init__(self):
        super().__init__()
        self.model = BertModel.from_pretrained('chambliss/distilbert-for-food-extraction')
        self.tokenizer = BertTokenizer.from_pretrained('distilbert')
        self.post_init()

    def _embed(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(text, return_tensors='pt').to(self.device)
        outputs = self.model(**inputs, output_hidden_states=True)
        return outputs.hidden_states[-1].detach().cpu().numpy()[0, 0, :].flatten()
    
    
class FoodBertEmbedderAvg(FoodBertEmbedder):
    def __init__(self):
        super().__init__()
    
    def _embed(self, text: str) -> np.ndarray:
        inputs = self.tokenizer(text, return_tensors='pt').to(self.device)
        outputs = self.model(**inputs)
        return outputs[0].detach().cpu().numpy().squeeze().mean(axis=0)
    
if __name__=="__main__":
    bert_embedder = FoodBertEmbedder()
    embed1 = bert_embedder.embed("BUTTERMILK PANCAKES BANANA FLAVOUR")
    embed2 = bert_embedder.embed("BUTTER WHOLE FAT")
    embed3 = bert_embedder.embed("BUTTERMILK")
    embed4 = bert_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)
    
    bert_embedder = FoodBertEmbedderAvg()
    embed1 = bert_embedder.embed("BUTTERMILK PANCAKES BANANA FLAVOUR")
    embed2 = bert_embedder.embed("BUTTER WHOLE FAT")
    embed3 = bert_embedder.embed("BUTTERMILK")
    embed4 = bert_embedder.embed("PANCAKES MADE FROM BUTTERMILK")
    similarity_matrix = cosine_similarity([embed1, embed2, embed3, embed4], [embed1, embed2, embed3, embed4])
    print(similarity_matrix)