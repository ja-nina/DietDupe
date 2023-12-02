from preprocessing.embedding_models.ensemble_embedder import EnsembleEmbedder
from preprocessing.clean_text import clean_text
from preprocessing.matcher import Matcher
from utils import masked_cosine_similarity
from pathlib import Path
import pandas as pd
import json

    
def load_internal_data(path: Path):
    internal_data= pd.read_csv(path)
    internal_data = internal_data.dropna(subset=['name'])
    internal_data['name'] =internal_data['name'].astype(str)
    internal_data_names = internal_data['name'].tolist()  
    indices_internal = internal_data['node_id'].tolist()
    return internal_data_names, indices_internal

def load_external_data(path: Path):
    external_data= pd.read_csv(path)
    external_data_names = external_data['Shrt_Desc'].tolist()
    return external_data_names

def save_output(output, output_directory: Path):
    output_directory.mkdir(parents=True, exist_ok=True)
    output.to_csv(output_directory / 'matching_full.csv', index=False)
    
    matching_dict = dict(zip(output['index_internal'], output['index_external']))
    
    with open(output_directory / 'matching_dict.json', 'w') as f:
        json.dump(matching_dict, f)
        
    
def match_flavougraph_nodes_to_nutridata(internal_data_path: Path, external_data_path: Path, output_directory: Path):
    names_internal, indices_internal = load_internal_data(internal_data_path)
    names_external = load_external_data(external_data_path)
    
    cleaned_internal_names = [clean_text(name) for name in names_internal]
    cleaned_external_names = [clean_text(name) for name in names_external]
    
    matcher_ensemble = Matcher(EnsembleEmbedder(), cleaned_internal_names, cleaned_external_names, similarity_function=masked_cosine_similarity, index_internal=indices_internal)
    results = matcher_ensemble.run()
    
    save_output(results, output_directory)
    
if __name__=='__main__':
    match_flavougraph_nodes_to_nutridata(internal_data_path=Path('data/nodes_191120.csv'), 
                                         external_data_path=Path('data/ABBREV.csv'),
                                         output_directory=Path('data/matches/'))
    