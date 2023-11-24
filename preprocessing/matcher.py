from preprocessing.hierarchical_matcher import HierarchicalMatcher
from preprocessing.embedding_models.bert_embedder import BertEmbedder
class Matcher:
    def __init__(self, model_for_embedding):
        self.list_of_names_matching = []
        self.list_of_names_to_match = []
        self.model_for_embedding = model_for_embedding
        self.hierarchical_matcher = HierarchicalMatcher(self.model_for_embedding)

    def create_embed_list(self, doc):
        augmanted_name_list = [list(self.hierarchical_matcher.hierarchical_stripper(name)) for name in self.list_of_names_to_match]
        return augmanted_name_list
    
if __name__=="__main__":
    # Test
    matcher = Matcher(BertEmbedder())
    matcher.list_of_names_to_match = ["This is a test sentence.", "This is a test sentence.", "This is a test sentence."]
    matcher.list_of_names_matching = ["This is a test sentence.", "This is a test sentence.", "This is a test sentence."]
    print(matcher.create_embed_list(matcher.list_of_names_to_match))
    print(matcher.create_embed_list(matcher.list_of_names_matching))