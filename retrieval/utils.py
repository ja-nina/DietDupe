from dataclasses import dataclass
from enum import Enum
from pathlib import Path

class CategoryOfRestriction(Enum):
    LOWER = 'lower'
    HIGHER ='higher'
    
class Nutrient(Enum):
    Water = "Water_(g)"
    Energ_Kcal = "Energ_Kcal"
    Protein = "Protein_(g)"
    Lipid_Tot = "Lipid_Tot_(g)"
    Ash = "Ash_(g)"
    Carbohydrt = "Carbohydrt_(g)"
    Fiber_TD = "Fiber_TD_(g)"
    Sugar_Tot = "Sugar_Tot_(g)"
    Calcium = "Calcium_(mg)"
    Iron = "Iron_(mg)"
    Magnesium = "Magnesium_(mg)"
    Phosphorus = "Phosphorus_(mg)"
    Potassium = "Potassium_(mg)"
    Sodium = "Sodium_(mg)"
    Zinc = "Zinc_(mg)"
    Copper = "Copper_mg)"
    Manganese = "Manganese_(mg)"
    Selenium = "Selenium_(�g)"
    Vit_C = "Vit_C_(mg)"
    Thiamin = "Thiamin_(mg)"
    Riboflavin = "Riboflavin_(mg)"
    Niacin = "Niacin_(mg)"
    Panto_acid = "Panto_Acid_mg)"
    Vit_B6 = "Vit_B6_(mg)"
    Folate_Tot = "Folate_Tot_(�g)"
    Folic_acid = "Folic_Acid_(�g)"
    Food_Folate = "Food_Folate_(�g)"
    Folate_DFE = "Folate_DFE_(�g)"
    Choline_Tot = "Choline_Tot_ (mg)"
    Vit_B12 = "Vit_B12_(�g)"
    Vit_A_IU = "Vit_A_IU"
    Vit_A_RAE = "Vit_A_RAE"
    Retinol = "Retinol_(�g)"
    Alpha_Carot = "Alpha_Carot_(�g)"
    Beta_Carot = "Beta_Carot_(�g)"
    Beta_Crypt = "Beta_Crypt_(�g)"
    Lycopene = "Lycopene_(�g)"
    Lut_Zea = "Lut+Zea_ (�g)"
    Vit_E = "Vit_E_(mg)"
    Vit_D_mcg = "Vit_D_�g"
    Vit_D_IU = "Vit_D_IU"
    Vit_K = "Vit_K_(�g)"
    FA_Sat = "FA_Sat_(g)"
    FA_Mono = "FA_Mono_(g)"
    FA_Poly = "FA_Poly_(g)"
    Cholestrl = "Cholestrl_(mg)"
    GmWt_1 = "GmWt_1"
    GmWt_Desc1 = "GmWt_Desc1"
    GmWt_2 = "GmWt_2"
    GmWt_Desc2 = "GmWt_Desc2"
    

@dataclass
class RecipeRestriction:
    category: CategoryOfRestriction
    nutrient: Nutrient
        