import os
import pandas as pd
import pickle

from dietdupe.retrieval.retriever_functions.retrieval_simple import retrieval_simple
from dietdupe.retrieval.retriever_functions.retrieval_with_restrictions import retrieval_with_restrictions
from dietdupe.utils import input_ingredients


class DietDupe:
    def __init__(self) -> None:
        self.matched_foods_cvs = "data/matches/matched_nutritional_data.csv"
        self.nutritional_data = "data/ABBREV.csv"
        self.full_matching = "data/matches/matching_full.csv"
        self.flavour_graph_embeddings = "data/FlavorGraph_node_embedding.pickle"
        self.flavour_graph_node_info = "data/nodes_191120.csv"
        
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
   
    def filter_by_nodes(self, food_embeddings):
        node_info = pd.read_csv(self.flavour_graph_node_info)
        node_info = node_info[(node_info['is_hub'] == 'hub') & (node_info['node_type'] == 'ingredient')]
        hub_ingredients = set(node_info['node_id'])
        food_embeddings_filtered = {key: value for key, value in food_embeddings.items() if key in hub_ingredients}
        return food_embeddings_filtered
        
    def get_embeddings(self):
        with open(self.flavour_graph_embeddings, "rb") as f:
            food_embeddings = pickle.load(f)
            food_embeddings = {int(key): value for key, value in food_embeddings.items()}
            food_embeddings = self.filter_by_nodes(food_embeddings)
            food_embeddings = dict(sorted(food_embeddings.items()))
        return food_embeddings
    
    def run(self, recipe_ingredients: list[str], restrictions = list[tuple[str, str]]):
        ingredients_matched = recipe_ingredients
        embeddings = self.get_embeddings()
        foods = self.load_foods()
        return retrieval_with_restrictions(foods, embeddings, ingredients_matched, 5, restrictions=restrictions)
    
if __name__ == '__main__':
    ingredients = input_ingredients() 
    res = DietDupe().run(recipe_ingredients = ingredients, restrictions = [("Protein_(g)", "lower")])
    print(res)
    
# parm cheese: 4615 ("Protein_(g)", "higher")
# poptata 5027 ("Carbohydrt_(g)", "lower")