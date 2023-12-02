# DietDupe
DietDupe: The flavourful Feat of Finding Fantastic Food Facsimiles

## Initial Plan

### Overall

By leveraging FlavorGraph, we can identify suitable substitutes for various
dietary preferences, such as vegan, keto, and low-carb, while maintaining
sensory satisfaction, ultimately enhancing the adherence and satisfaction of
individuals following these diets.

By using the output of our DD module we could inject it into the reverse-cooking
pipeline and make it produce sensible recipes.

### Steps

1. Research
2. Finding a database of food categories(example: vegan, paleo, keto, low carb,
   etc.)
3. Provide a mapping to FlavourGraph
4. EXPERIMENT with approaches
5. Pick best approach

### Literature

- FlavourGraph <https://github.com/lamypark/FlavorGraph>
- inverse cooking <https://github.com/facebookresearch/inversecooking>

### Datasets

- FoodDB (see in data folder - used description for possibble finetuning),
- FlavourGraph,
- dataset of food classification by food category (or nutriscore)
- [USDA National Nutrient Database for Standard Reference, Release 27](http://www.ars.usda.gov/ba/bhnrc/ndl), abbreviations will be used from [abbreviations APPENDIX A](https://data.nal.usda.gov/dataset/composition-foods-raw-processed-prepared-usda-national-nutrient-database-standard-referen-14)
- things 2 try: https://github.com/chambliss/foodbert

### 
TODO: ADD INSTRUCTIONS ABOUT KAGGLE NB AND INFO ABOUT HUGGINGFACE AND WB API KEYS