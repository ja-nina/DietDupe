import json

import pandas as pd
import streamlit as st

from dietdupe.retrieval.diet_dupe import DietDupe
from dietdupe.retrieval import Nutrient, RecipeRestriction


def get_products():
    products = pd.read_csv('data/nodes_191120.csv')
    products = products[products['is_hub'] == 'hub']
    products = products[products['node_type'] == 'ingredient']
    products = products.drop(columns=['id', 'is_hub', 'node_type'])
    return products


def get_categories():
    categories = [
        "Water", "Energ_Kcal", "Protein", "Lipid_Tot", "Ash", "Carbohydrt",
        "Fiber_TD", "Sugar_Tot", "Calcium", "Iron", "Magnesium", "Phosphorus",
        "Potassium", "Sodium", "Zinc", "Copper", "Manganese", "Selenium_", "Vit_C",
        "Thiamin", "Riboflavin", "Niacin", "Panto_Acid", "Vit_B6", "Folate_Tot_",
        "Folic_Acid", "Food_Folate_", "Folate_DFE", "Choline_Tot", "Vit_B12", "Vit_A_IU",
        "Vit_A_RAE", "Retinol", "Alpha_Carot", "Beta_Carot", "Beta_Crypt", "Lycopene_",
        "Lut_Zea_ ", "Vit_E", "Vit_D_µg", "Vit_D_IU", "Vit_K", "FA_Sat", "FA_Mono", "FA_Poly",
        "Cholestrl"
    ]
    return categories


def get_restrictions():
    return ['lower', 'higher']


def get_nutritional_data():
    nutritional_data = pd.read_csv('data/ABBREV.csv')
    return nutritional_data


def get_matchings():
    with open('data/matches/matching_dict.json', 'r') as f:
        d = json.load(f)
    return d


def get_matched_nutritional_data():
    matched_nutritional_data = pd.read_csv('data/matches/matched_nutritional_data.csv')
    return matched_nutritional_data


def format_selected_products(products, matchings, nutritional_data, selected_products, selected_restrictions):
    matched_products = [matchings[str(products[products['name'] == p]['node_id'].tolist()[0])] for p in
                        selected_products]

    df = pd.DataFrame()
    df['selected'] = [p for p in selected_products]
    # FIXME: show matched names
    # df['matched'] = matched_products
    for r in selected_restrictions:
        df[r] = [nutritional_data[nutritional_data['index'] == p][Nutrient[r].value].tolist()[0] for p in
                 matched_products]
    return df


def propose_products(diet_dupe: DietDupe, products, nutritional_data, selected_product, selected_restrictions):
    product_id = products[products['name'] == selected_product]['node_id'].tolist()
    proposal_names = diet_dupe.run(product_id, [
        RecipeRestriction(category=v, nutrient=Nutrient[k]) for k, v in selected_restrictions.items()])
    proposal = pd.DataFrame()
    proposal['name'] = proposal_names

    # todo: show nutritional data for replacements
    # for r in selected_restrictions:
    #     proposal[r] = [nutritional_data[nutritional_data['internal'] == p][r].tolist()[0] for p in proposal_names]
    return proposal


def main():
    products = get_products()
    nutritional_data = get_nutritional_data()
    matchings = get_matchings()
    categories = get_categories()
    restrictions = get_restrictions()
    diet_dupe = DietDupe()

    st.title('DietDupe')

    selected_products = st.sidebar.multiselect(
        'Select Products',
        products['name'].tolist()
    )

    selected_categories = st.sidebar.multiselect(
        'Select Categories',
        categories
    )

    selected_restrictions = {}
    for category in selected_categories:
        restraint = st.sidebar.radio(f"Select restriction for {category}", restrictions)
        selected_restrictions[category] = restraint

    st.subheader('Selected Products:')
    st.write(format_selected_products(products,
                                      matchings, nutritional_data, selected_products, selected_restrictions))

    if st.sidebar.button('Confirm Selection'):
        for selected_product in selected_products:
            st.subheader(f"Related products for {selected_product} with selected restrictions:")
            related_products = propose_products(
                diet_dupe, products, nutritional_data, selected_product, selected_restrictions)
            st.write(related_products)


if __name__ == '__main__':
    main()
