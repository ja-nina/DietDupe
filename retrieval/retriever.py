import os
import pandas as pd
import pickle

from retrieval.retriever_functions.retrieval_simple import retrieval_simple
from retrieval.retriever_functions.retrieval_with_restrictions import retrieval_with_restrictions
from utils import input_ingredients


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
            food_embeddings = {key: value for key, value in food_embeddings.items() if key < 7102} # FIXME: hard-coded non-compounds
            food_embeddings = dict(sorted(food_embeddings.items()))
        return food_embeddings
    
    def run(self, recipe_ingredients: list[str], restrictions = list[tuple[str, str]]):
        ingredients_matched = recipe_ingredients
        embeddings = self.get_embeddings()
        foods = self.load_foods()
        return retrieval_with_restrictions(foods, embeddings, ingredients_matched, 5, restrictions=restrictions)
    
if __name__ == '__main__':
    ingredients = input_ingredients() 
    res = DietDupe().run(recipe_ingredients = ingredients, restrictions = [("Protein_(g)", "higher")])
    print(res)