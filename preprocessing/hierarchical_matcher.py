class HierarchicalMatcher:
    def __init__(self, embedding_model):
        self.model = embedding_model

    def hierarchy_stripper(self, hierarchical_text: list[str]):
        for i in range(1,len(hierarchical_text)):
            yield hierarchical_text[:-i]
    
    def get_embedding(self, word: str):
        self.model.get_embedding(word)
        
if __name__=="__main__":
    # Test
    hierarchical_text = ["This", "is", "a", "test", "sentence."]
    matcher = HierarchicalMatcher(None)
    for i in matcher.hierarchy_stripper(hierarchical_text):
        print(i)
        