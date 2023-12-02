import pandas as pd
import logging
import os
import pickle
from tqdm.auto import tqdm
from retrieval.retriever_functions.simple_retreiver import simple_similarity_distance

logging.basicConfig(level=logging.INFO)
class DietDupe:
    def __init__(self) -> None:
        self.matched_foods_cvs = "data/matches/matched_nutritional_data.csv"
        self.nutritional_data = "data/ABBREV.csv"
        self.full_matching = "data/matches/matching_full.csv"
        self.flavour_graph_embeddings = "data/FlavorGraph_node_embedding.pickle"
        
    def load_foods(self):
        if not os.path.exists(self.matched_foods_cvs):
            foods = pd.read_csv(self.nutritional_data, index_col=0)
            with open(self.full_matching, "r") as f:
                matches_full = pd.read_csv(self.full_matching, index_col=1)

            food_filtered = foods.merge(matches_full, left_index=True, right_on='index_external')
            food_filtered.to_csv(self.matched_foods_cvs)
            
            return food_filtered
        else:
            return pd.read_csv(self.matched_foods_cvs).set_index("index_internal")
        
    def get_embeddings(self):
        with open(self.flavour_graph_embeddings, "rb") as f:
            food_embeddings = pickle.load(f)
            food_embeddings = {int(key): value for key, value in food_embeddings.items()}
            food_embeddings = {key: value for key, value in food_embeddings.items() if key < 7102}
            food_embeddings = dict(sorted(food_embeddings.items()))
        return food_embeddings
    
    def run(self, recipe_ingredients: list[str]):
        ingredients_matched = recipe_ingredients
        embeddings = self.get_embeddings()
        foods = self.load_foods()
        return simple_similarity_distance(foods, embeddings, recipe_indices = ingredients_matched, top_k=5)
res = DietDupe().run([158])
print(res)