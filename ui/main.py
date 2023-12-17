import pandas as pd
import streamlit as st

from retrieval.retriever import DietDupe


def get_products():
    products = pd.read_csv('data/nodes_191120.csv')
    products = products[products['is_hub'] == 'hub']
    products = products[products['node_type'] == 'ingredient']
    products = products.drop(columns=['id', 'is_hub', 'node_type'])
    return products


def get_categories():
    categories = [
        "Water_(g)", "Energ_Kcal", "Protein_(g)", "Lipid_Tot_(g)", "Ash_(g)", "Carbohydrt_(g)", "Fiber_TD_(g)",
        "Sugar_Tot_(g)", "Calcium_(mg)", "Iron_(mg)", "Magnesium_(mg)", "Phosphorus_(mg)", "Potassium_(mg)",
        "Sodium_(mg)", "Zinc_(mg)", "Copper_mg)", "Manganese_(mg)", "Selenium_(µg)", "Vit_C_(mg)",
        "Thiamin_(mg)", "Riboflavin_(mg)", "Niacin_(mg)", "Panto_Acid_mg)", "Vit_B6_(mg)", "Folate_Tot_(µg)",
        "Folic_Acid_(µg)", "Food_Folate_(µg)", "Folate_DFE_(µg)", "Choline_Tot_ (mg)", "Vit_B12_(µg)", "Vit_A_IU",
        "Vit_A_RAE", "Retinol_(µg)", "Alpha_Carot_(µg)", "Beta_Carot_(µg)", "Beta_Crypt_(µg)", "Lycopene_(µg)",
        "Lut+Zea_ (µg)", "Vit_E_(mg)", "Vit_D_µg", "Vit_D_IU", "Vit_K_(µg)", "FA_Sat_(g)", "FA_Mono_(g)",
        "FA_Poly_(g)", "Cholestrl_(mg)"
    ]
    return categories


def get_restrictions():
    return ['lower', 'higher']


def get_nutritional_data():
    nutritional_data = pd.read_csv('data/ABBREV.csv')
    return nutritional_data


def get_matched_nutritional_data():
    matched_nutritional_data = pd.read_csv('data/matches/matched_nutritional_data.csv')
    return matched_nutritional_data


def format_selected_products(matched_data, nutritional_data, selected_products, selected_restrictions):
    matched_products = [matched_data[matched_data['internal'] == p]['Shrt_Desc'].tolist()[0] for p in selected_products]

    df = pd.DataFrame()
    df['selected'] = [p for p in selected_products]
    df['matched'] = matched_products
    for r in selected_restrictions:
        df[r] = [nutritional_data[nutritional_data['Shrt_Desc'] == p][r].tolist()[0] for p in matched_products]
    return df


def propose_products(diet_dupe: DietDupe, products, nutritional_data, selected_product, selected_restrictions):
    product_id = products[products['name'] == selected_product]['node_id'].tolist()
    # FIXME:
    # proposal_names = diet_dupe.run(product_id, [(k, v) for k, v in selected_restrictions.items()])
    proposal_names = ["TOFU,FRIED", "CHEESE,CAMEMBERT"]
    proposal = pd.DataFrame({'name': proposal_names})
    for r in selected_restrictions:
        proposal[r] = [nutritional_data[nutritional_data['Shrt_Desc'] == p][r].tolist()[0] for p in proposal_names]
    return proposal


def main():
    products = get_products()
    nutritional_data = get_nutritional_data()
    matched_nutritional_data = get_matched_nutritional_data()
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
    st.write(format_selected_products(
        matched_nutritional_data, nutritional_data, selected_products, selected_restrictions))

    if st.sidebar.button('Confirm Selection'):
        for selected_product in selected_products:
            st.subheader(f"Related products for {selected_product} with selected restrictions:")
            related_products = propose_products(
                diet_dupe, products, nutritional_data, selected_product, selected_restrictions)
            st.write(related_products)


if __name__ == '__main__':
    main()
