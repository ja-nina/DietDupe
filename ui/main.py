import streamlit as st
import pandas as pd

# TODO: proper list of products (from embeddings)
# Load the list of products from CSV file
products_df = pd.read_csv('data/matches/matched_nutritional_data.csv')

# TODO: load categories from file
categories = "Water_(g),Energ_Kcal,Protein_(g),Lipid_Tot_(g),Ash_(g),Carbohydrt_(g),Fiber_TD_(g),Sugar_Tot_(g),Calcium_(mg),Iron_(mg),Magnesium_(mg),Phosphorus_(mg),Potassium_(mg),Sodium_(mg),Zinc_(mg),Copper_mg),Manganese_(mg),Selenium_(µg),Vit_C_(mg),Thiamin_(mg),Riboflavin_(mg),Niacin_(mg),Panto_Acid_mg),Vit_B6_(mg),Folate_Tot_(µg),Folic_Acid_(µg),Food_Folate_(µg),Folate_DFE_(µg),Choline_Tot_ (mg),Vit_B12_(µg),Vit_A_IU,Vit_A_RAE,Retinol_(µg),Alpha_Carot_(µg),Beta_Carot_(µg),Beta_Crypt_(µg),Lycopene_(µg),Lut+Zea_ (µg),Vit_E_(mg),Vit_D_µg,Vit_D_IU,Vit_K_(µg),FA_Sat_(g),FA_Mono_(g),FA_Poly_(g),Cholestrl_(mg),GmWt_1,GmWt_Desc1,GmWt_2,GmWt_Desc2,Refuse_Pct,NDB_No_x,Shrt_Desc_x,Water_(g)_x,Energ_Kcal_x,Protein_(g)_x,Lipid_Tot_(g)_x,Ash_(g)_x,Carbohydrt_(g)_x,Fiber_TD_(g)_x,Sugar_Tot_(g)_x,Calcium_(mg)_x,Iron_(mg)_x,Magnesium_(mg)_x,Phosphorus_(mg)_x,Potassium_(mg)_x,Sodium_(mg)_x,Zinc_(mg)_x,Copper_mg)_x,Manganese_(mg)_x,Selenium_(µg)_x,Vit_C_(mg)_x,Thiamin_(mg)_x,Riboflavin_(mg)_x,Niacin_(mg)_x,Panto_Acid_mg)_x,Vit_B6_(mg)_x,Folate_Tot_(µg)_x,Folic_Acid_(µg)_x,Food_Folate_(µg)_x,Folate_DFE_(µg)_x,Choline_Tot_ (mg)_x,Vit_B12_(µg)_x,Vit_A_IU_x,Vit_A_RAE_x,Retinol_(µg)_x,Alpha_Carot_(µg)_x,Beta_Carot_(µg)_x,Beta_Crypt_(µg)_x,Lycopene_(µg)_x,Lut+Zea_ (µg)_x,Vit_E_(mg)_x,Vit_D_µg_x,Vit_D_IU_x,Vit_K_(µg)_x,FA_Sat_(g)_x,FA_Mono_(g)_x,FA_Poly_(g)_x,Cholestrl_(mg)_x,GmWt_1_x,GmWt_Desc1_x,GmWt_2_x,GmWt_Desc2_x,Refuse_Pct_x,NDB_No.1,Shrt_Desc_y,Water_(g)_y,Energ_Kcal_y,Protein_(g)_y,Lipid_Tot_(g)_y,Ash_(g)_y,Carbohydrt_(g)_y,Fiber_TD_(g)_y,Sugar_Tot_(g)_y,Calcium_(mg)_y,Iron_(mg)_y,Magnesium_(mg)_y,Phosphorus_(mg)_y,Potassium_(mg)_y,Sodium_(mg)_y,Zinc_(mg)_y,Copper_mg)_y,Manganese_(mg)_y,Selenium_(µg)_y,Vit_C_(mg)_y,Thiamin_(mg)_y,Riboflavin_(mg)_y,Niacin_(mg)_y,Panto_Acid_mg)_y,Vit_B6_(mg)_y,Folate_Tot_(µg)_y,Folic_Acid_(µg)_y,Food_Folate_(µg)_y,Folate_DFE_(µg)_y,Choline_Tot_ (mg)_y,Vit_B12_(µg)_y,Vit_A_IU_y,Vit_A_RAE_y,Retinol_(µg)_y,Alpha_Carot_(µg)_y,Beta_Carot_(µg)_y,Beta_Crypt_(µg)_y,Lycopene_(µg)_y,Lut+Zea_ (µg)_y,Vit_E_(mg)_y,Vit_D_µg_y,Vit_D_IU_y,Vit_K_(µg)_y,FA_Sat_(g)_y,FA_Mono_(g)_y,FA_Poly_(g)_y,Cholestrl_(mg)_y,GmWt_1_y,GmWt_Desc1_y,GmWt_2_y,GmWt_Desc2_y,Refuse_Pct_y,NDB_No_y,Shrt_Desc_x.1,Water_(g)_x.1,Energ_Kcal_x.1,Protein_(g)_x.1,Lipid_Tot_(g)_x.1,Ash_(g)_x.1,Carbohydrt_(g)_x.1,Fiber_TD_(g)_x.1,Sugar_Tot_(g)_x.1,Calcium_(mg)_x.1,Iron_(mg)_x.1,Magnesium_(mg)_x.1,Phosphorus_(mg)_x.1,Potassium_(mg)_x.1,Sodium_(mg)_x.1,Zinc_(mg)_x.1,Copper_mg)_x.1,Manganese_(mg)_x.1,Selenium_(µg)_x.1,Vit_C_(mg)_x.1,Thiamin_(mg)_x.1,Riboflavin_(mg)_x.1,Niacin_(mg)_x.1,Panto_Acid_mg)_x.1,Vit_B6_(mg)_x.1,Folate_Tot_(µg)_x.1,Folic_Acid_(µg)_x.1,Food_Folate_(µg)_x.1,Folate_DFE_(µg)_x.1,Choline_Tot_ (mg)_x.1,Vit_B12_(µg)_x.1,Vit_A_IU_x.1,Vit_A_RAE_x.1,Retinol_(µg)_x.1,Alpha_Carot_(µg)_x.1,Beta_Carot_(µg)_x.1,Beta_Crypt_(µg)_x.1,Lycopene_(µg)_x.1,Lut+Zea_ (µg)_x.1,Vit_E_(mg)_x.1,Vit_D_µg_x.1,Vit_D_IU_x.1,Vit_K_(µg)_x.1,FA_Sat_(g)_x.1,FA_Mono_(g)_x.1,FA_Poly_(g)_x.1,Cholestrl_(mg)_x.1,GmWt_1_x.1,GmWt_Desc1_x.1,GmWt_2_x.1,GmWt_Desc2_x.1,Refuse_Pct_x.1,index_internal,Shrt_Desc_y.1,Water_(g)_y.1,Energ_Kcal_y.1,Protein_(g)_y.1,Lipid_Tot_(g)_y.1,Ash_(g)_y.1,Carbohydrt_(g)_y.1,Fiber_TD_(g)_y.1,Sugar_Tot_(g)_y.1,Calcium_(mg)_y.1,Iron_(mg)_y.1,Magnesium_(mg)_y.1,Phosphorus_(mg)_y.1,Potassium_(mg)_y.1,Sodium_(mg)_y.1,Zinc_(mg)_y.1,Copper_mg)_y.1,Manganese_(mg)_y.1,Selenium_(µg)_y.1,Vit_C_(mg)_y.1,Thiamin_(mg)_y.1,Riboflavin_(mg)_y.1,Niacin_(mg)_y.1,Panto_Acid_mg)_y.1,Vit_B6_(mg)_y.1,Folate_Tot_(µg)_y.1,Folic_Acid_(µg)_y.1,Food_Folate_(µg)_y.1,Folate_DFE_(µg)_y.1,Choline_Tot_ (mg)_y.1,Vit_B12_(µg)_y.1,Vit_A_IU_y.1,Vit_A_RAE_y.1,Retinol_(µg)_y.1,Alpha_Carot_(µg)_y.1,Beta_Carot_(µg)_y.1,Beta_Crypt_(µg)_y.1,Lycopene_(µg)_y.1,Lut+Zea_ (µg)_y.1,Vit_E_(mg)_y.1,Vit_D_µg_y.1,Vit_D_IU_y.1,Vit_K_(µg)_y.1,FA_Sat_(g)_y.1,FA_Mono_(g)_y.1,FA_Poly_(g)_y.1,Cholestrl_(mg)_y.1,GmWt_1_y.1,GmWt_Desc1_y.1,GmWt_2_y.1,GmWt_Desc2_y.1,Refuse_Pct_y.1".split(",")

# TODO: replace with retriever
# Function to propose a list of products for a selected product and categories
def propose_products(selected_product, selected_categories, category_options):
    # Replace this function with your own logic for proposing products
    # For demonstration purposes, we'll just return a simple list.
    return [f"Related Product {i}" for i in range(1, 4)]


# Streamlit App
def main():
    st.title('Product Selector App')

    # Sidebar with product selection
    selected_products = st.sidebar.multiselect(
        'Select Products',
        products_df['Shrt_Desc'].tolist()
    )

    # Sidebar with category and option selection
    selected_categories = st.sidebar.multiselect(
        'Select Categories',
        # products_df['Category'].unique().tolist()
        categories
    )

    category_options = {}
    for category in selected_categories:
        option = st.sidebar.radio(f"Select option for {category}", ['LOWER', 'HIGHER'])
        category_options[category] = option

    # Search bar for product selection
    search_query = st.sidebar.text_input('Search Products', '')

    # Filter products based on search query and selected categories
    filtered_products = products_df[products_df['Shrt_Desc'].str.contains(search_query, case=False)]

    # Display filtered products in the main area
    st.subheader('Available Products:')
    st.write(filtered_products)

    # Display selected products
    st.subheader('Selected Products:')
    st.write(selected_products)

    # Confirm button
    if st.sidebar.button('Confirm Selection'):
        # Display related products for each selected product and categories
        for selected_product in selected_products:
            st.subheader(f"Related products for {selected_product} with selected constraints:")
            related_products = propose_products(selected_product, selected_categories, category_options)
            st.write(related_products)


if __name__ == '__main__':
    main()
