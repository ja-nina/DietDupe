import re
import enchant
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

en_dict = enchant.Dict("en_US")
word_whitelist_regex = re.compile(r"\d+%?")
def is_english_word(s: str) -> bool:
    return en_dict.check(s) or word_whitelist_regex.match(s)

nltk.download("stopwords")
nltk.download("wordnet")
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Hard-coded, hand-made regex for splitting words, but 
split_regex = re.compile(r"[|\s()&_]+")
abbrev_map = {
    "w/": "with",
    "lrg": "large",
    "sml": "small",
    "crmd": "creamed",
    "uncrmd": "",
    "lowfat": "low fat",
    "milkfat": "milk fat",
    "ckd": "cooked",
    "cnd": "canned",
    "frz": "frozen",
    "rstd": "roasted",
    "bnless": "boneless",
    "bld": "boiled",
    "frsh": "fresh",
    "ln": "lean",
    "brst": "breast",
    "babyfood": "baby food",
    "choic": "choice",
    "whl": "whole",
    "h2o": "water",
    "drnd": "drained",
    "skn": "skin",
    "brsd": "braised",
    "pan-fried": "fried",
    "chs": "chips",
    "grds": "grades",
    "stmd": "steamed",
    "unprep": "unprepared",
    "rnd": "round",
    "nz": "",  # stands for New Zealand as far as I can tell; not relevant?
    "brld": "broiled",
    "juc": "juice",
    "sel": "select",  # not very sure, but it seems plausible (https://www.usda.gov/media/blog/2013/01/28/whats-your-beef-prime-choice-or-select)
    "shldr": "shoulder",
    "crm": "cream",
    "stk": "steak",
    "pln": "plain",
    "pdr": "powder",
    "cond": "condensed",
    "sau": "sauce",
    "bev": "beverage",
    "condmnt": "condiment",
    "soybn": "soybean",
    "rst": "roast",
    'lt': 'light',
    'lo': 'low',
    'na': 'sodium',
    'dom': 'domestic',
    'sndwch': 'sandwich',
    'swt': 'sweet',
    'drk': 'drink',
    'mxd': 'mixed',
    'appl': 'apple',
    'choc': 'chocolate',
    'bkd': 'baked',
    'bns': 'beans',
    'rts': 'ready-to-serve',
    'enr': 'enriched',
    'flr': 'flour',
    'vit': 'vitamin',
    'str': 'strawberry',
    'grn': 'green',
    'crl': 'cereal',
    'rtl': 'retail',
    'quaker': 'quaker (brand)',
    'kashi': 'kashi (brand)',
    'bnls': 'boneless',
    'yel': 'yellow',
    'mcdonald\'s': 'mcdonald\'s (brand)',
    'drsng': 'dressing',
    'cntr': 'center',
    'unswtnd': 'unsweetened',
    'dk': 'dark',
    'unenr': 'unenriched',
    'cinn': 'cinnamon',
    'pnut': 'peanut',
    'commly': 'commonly',
    'kellogg': 'kellogg',
    'eq': 'equal',
    'shrt': 'short',
    'htd': 'heated',
    'frstd': 'frosted',
    'bttm': 'bottom',
    'sp': 'species',
    'unhtd': 'unheated',
    'prot': 'protein',
    'lofat': 'low fat',
    'usda': 'united states department of agriculture',
    'conc': 'concentrate',
    'soln': 'solution',
    'chk': 'chuck',
    'swtnd': 'sweetened',
    'rtf': 'ready to feed',
    'stwd': 'stewed',
    'morningstar': 'morningstar farms (brand)',
    'grld': 'grilled',
    'lip-on': 'lip-on',
    'sprd': 'spread',
    'hvy': 'heavy',
    'btld': 'bottled',
    'nat': 'natural',
    'tstd': 'toasted',
    'chinese': 'chinese',
    'spl': 'special',
    'drumstk': 'drumstick',
    'snackfood': 'snack food',
    'dssrt': 'dessert',
    'johnson': 'johnson',
    'nutr': 'nutrient',
    'eggo': 'eggo (brand)',
    'brkfst': 'breakfast',
    'krnls': 'kernels',
    'dha': 'docosahexaenoic acid',
    'cocnt': 'coconut',
    'immat': 'immature',
    'murray': 'murray (brand)',
    'ara': 'arachidonic acid',
    'refr': 'refrigerated',
    'stks': 'sticks',
    'simmrd': 'simmered',
    'malt-o-meal': 'cereal',
    'v8': 'vegetable juice',
    'stk/rst': 'steak or roast',
    'hydr': 'hydrated',
    'bttrmlk': 'buttermilk',
    'flav': 'flavor',
    'enfamil': 'infant formula',
    'gluten-free': 'gluten-free',
    'atlantic': 'Atlantic',
    'pepperidge': 'Pepperidge Farm',
    'rtd': 'ready-to-drink',
    'pop-tarts': 'Pop-Tarts',
    'chopd': 'chopped',
    'cheez-it': 'Cheez-It',
    'pudd': 'pudding',
    'bbq': 'barbecue',
    'pnuts': 'peanuts',
    'pnappl': 'pineapple',
    'art': 'artificial',
    'swtnr': 'sweetener',
    'cttnsd': 'cottonseed',
    'frstng': 'frosting',
    'rtb': 'ready-to-bake',
    'coatd': 'coated',
    'asprt': 'aspartame',
    'rth': 'ready-to-heat',
    'tlc': 'tasty little crackers',
    'cheeseburger;': 'cheeseburger',
    "'n'": 'and',
    'wgu': 'wagyu',
    "denny's": "denny's",
    'bsd': 'based',
    'simil': 'similac',
    'grns': 'greens',
    'wntr': 'winter',
    'fd': 'food',
    'todd': 'toddler',
    'unckd': 'uncooked',
    'sirl': 'sirloin',
    'carb': 'carbonated',
    'rw': "raw",
    'smmr': "summer",
    'bnl': "boneless",
    'aus': 'australian',
    'cmdty': 'commodity.',
    'lttc': 'lettuce',
    'au': 'with juice',
    'chck': "meat chuck",
    'marshmllw': 'marshmallow.',
    'wht': 'white',
    'imitn': 'imitation',
    'grd': 'ground',
    'tp': 'top',
    'und': 'undercut',
    "w/": "with"
}

def expand_abbreviations(nutri_foods: list[str]):
    """
    Expand abbreviations in the nutridata dataset.
    """
    for abbrev in abbrev_map:
        text = text.replace(abbrev, abbrev_map[abbrev])
    return text

def process_abbreviations(tokens: str):
    tokens_new = []
    tokens_abbrev_expanded = []
    i = 0
    while i < len(tokens):
        if tokens[i] in ("without", "w/o", "wo/"): 
            i += 2  
            continue
        if tokens[i].startswith("wo/") :
            i += 2 
            continue
        tokens_new.append(tokens[i])
        i += 1
        
    tokens_abbrev_expanded = [abbrev_map[token].lower() if token in abbrev_map else token for token in tokens_new]
    tokens_abbrev_expanded = list(map(lemmatizer.lemmatize, tokens_abbrev_expanded))
    return " ".join(tokens_abbrev_expanded)

def clean_text(txt: str) -> str:
    text_with_with_comma = txt.replace(",", " , ").replace("W/", "W/ ") 
    tokens = split_regex.split(text_with_with_comma.lower())   
    text_clean = process_abbreviations(tokens)
    
    return text_clean

if __name__ == "__main__":
    text = "CHEESE,COTTAGE,CRMD,W/FRUIT"
    print(clean_text(text))