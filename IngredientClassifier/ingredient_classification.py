import json

with open('final_ingredients.json') as data_file:
    data = json.load(data_file)

filtered = [ing for ing in data if 'name' in ing]


def keyword_in_related(keyword, related_ingredients):
    for ingredient in related_ingredients:
        if keyword in ingredient['name'].lower():
            return True
    return False


def keyword_in_name(ingredient, keyword):
    if keyword in ingredient['name'].lower():
        return True
    return keyword_in_related(keyword, ingredient['relatedIngredients'])


def ingredients_with_keyword(ingredients, keyword):
    return [ingredient for ingredient in ingredients if keyword_in_name(ingredient, keyword)]


def get_all_with_keyword(keyword):
    return ingredients_with_keyword(filtered, keyword)


def get_with_keywords(words):
    all_ingredients = list()
    for word in words:
        all_ingredients = all_ingredients + get_all_with_keyword(word)
    return all_ingredients


def add_color(ingredients, color):
    for ing in ingredients:
        ing.update({'color': color})
    return ingredients


def add_category(ingredients, category):
    for ing in ingredients:
        ing.update({'category' : category})
    return ingredients


def remove_duplicates_by_id(ingredients):
    seen = set()
    return [x for x in ingredients if x['id'] not in seen and not seen.add(x['id'])]


def make_final_dict(baseid, category, color, ingredient):
    return {'Name' : ingredient['name'], 'ID' : ingredient['id'], 'Color' : color, 'Category' : category, 'BaseID' : baseid}


def convert_to_final(base_ingredient):
    if 'color' in base_ingredient:
        return [{'Name' : base_ingredient['name'], 'ID' : base_ingredient['id'], 'Color' : base_ingredient['color'], 'Category' : base_ingredient['category'], 'BaseID' : base_ingredient['id']}] +\
               [make_final_dict(base_ingredient['id'], base_ingredient['category'], base_ingredient['color'], related) for related in base_ingredient['relatedIngredients']]
    return [{'Name' : base_ingredient['name'], 'ID' : base_ingredient['id'], 'Category' : base_ingredient['category'], 'BaseID' : base_ingredient['id']}] + [make_final_dict(base_ingredient['id'], base_ingredient['category'], "", related) for related in base_ingredient['relatedIngredients']]


neutral_spirits = get_with_keywords(['gin', 'vodka', 'jenever'])
neutral_spirits = add_color(neutral_spirits, 'light blue')

liqueurs_and_schnapps = get_with_keywords(['liqueur', 'schnapps', 'amaro', 'picon', 'chartreuse', 'licor'])
liqueurs_and_schnapps = add_color(liqueurs_and_schnapps, 'tan')

whiskies = get_with_keywords(['whiskey', 'scotch', 'bourbon'])
whiskies = add_color(whiskies, 'brown')

rum = get_all_with_keyword('rum')
rum = add_color(rum, 'brown')

wine = get_with_keywords(['wine', 'sherry', 'lillet', 'mad dog'])
wine = add_color(wine, 'purple')

brandy = get_all_with_keyword('brandy')
brandy = add_color(brandy, 'brown')

beer = [ing for ing in filtered if ('beer' in ing['name'].lower() and ('root' not in ing['name'].lower() and 'ginger' not in ing['name'].lower() and ing not in liqueurs_and_schnapps))]
beer = add_color(beer, 'brown')

cachaca = get_all_with_keyword('cachaca')
cachaca = add_color(cachaca, 'light blue')

pisco = get_all_with_keyword('pisco')
pisco = add_color(pisco, 'light blue')

fernet = get_all_with_keyword('fernet')
fernet = add_color(fernet, 'purple')

aquavit = get_all_with_keyword('aquavit')
aquavit = add_color(aquavit, 'tan')

champagne = [ing for ing in filtered if ('champagne' in ing['name'].lower() and 'soda' not in ing['name'].lower())]
champagne = add_color(champagne, 'yellow')

arrack = get_all_with_keyword('arrack')
arrack = add_color(arrack, 'brown')

japanese_drinks = get_with_keywords(['shochu', 'sake'])
japanese_drinks = add_color(japanese_drinks, 'light blue')

tequila = get_with_keywords(['tequila', 'mezcal'])
tequila = add_color(tequila, 'light blue')

port = get_all_with_keyword('port')
port = add_color(port, 'purple')

irish_mist = get_all_with_keyword('mist')
irish_mist = add_color(irish_mist, 'brown')

firewater = get_with_keywords(['firewater'])
firewater = add_color(firewater, 'brown')

absinthe = get_with_keywords(['absinthe'])
absinthe = add_color(absinthe, 'green')

mandarin_napoleon = get_all_with_keyword('napoleon')
mandarin_napoleon = add_color(mandarin_napoleon, 'brown')

hard_lemonade = get_all_with_keyword('hard lemonade')
hard_lemonade = add_color(hard_lemonade, 'yellow')

cider = get_with_keywords(['hard cider', 'cherry cider', 'strongbow cider'])
cider = add_color(cider, 'red')

zima = get_all_with_keyword('zima')
zima = add_color(zima, 'tan')

taboo = get_all_with_keyword('taboo')
taboo = add_color(taboo, 'brown')

vermouth = get_all_with_keyword('vermouth')
vermouth = add_color(vermouth, 'tan')

jager = get_all_with_keyword('jagermeister')
jager = add_color(jager, 'dark brown')

alcohols = rum + whiskies + liqueurs_and_schnapps + neutral_spirits + wine + brandy + beer + cachaca + pisco + fernet + \
           aquavit + champagne + arrack + japanese_drinks + tequila + port + firewater + absinthe + mandarin_napoleon + cider + irish_mist + hard_lemonade + zima + taboo + vermouth + jager


soda = get_with_keywords(['soda', 'coke', 'grenadine'])
soda = add_color(soda, 'dark red')

water = get_all_with_keyword('water')
water = add_color(water, 'light blue')

kool_aide = get_with_keywords(['aide', 'aid'])
kool_aide = add_color(kool_aide, 'red')

juice = [ing for ing in get_with_keywords(['juice']) if ing not in alcohols]
juice = add_color(juice, 'purple')

mixes = get_all_with_keyword('mix')
mixes = add_color(mixes, 'yellow')

milk = get_with_keywords(['milk', 'half and half'])
milk = add_color(milk, 'white')

nectar = get_with_keywords(['nectar'])
nectar = add_color(nectar, 'orange')

hot_chocolate = get_all_with_keyword('hot chocolate')
hot_chocolate = add_color(hot_chocolate, 'creamy brown')

cream = get_with_keywords(['heavy cream', 'light cream'])
cream = add_color(cream, 'white')

ginger_shit = get_with_keywords(['ginger ale', 'ginger beer'])
ginger_shit = add_color(ginger_shit, 'yellow')

tea = [ing for ing in get_with_keywords(['tea', 'snapple']) if (ing not in alcohols and ing not in mixes)]
tea = add_color(tea, 'brown')

soft_cider = [ing for ing in get_all_with_keyword('cider') if ing not in cider]
soft_cider = add_color(soft_cider, 'brown')

lemonade = [ing for ing in get_with_keywords(['lemonade', 'limeade']) if ing not in alcohols]
lemonade = add_color(lemonade, 'yellow')

mello_yello = get_all_with_keyword('mello')
mello_yello = add_color(mello_yello, 'yellow')

sprite = get_all_with_keyword('sprite')
sprite = add_color(sprite, 'light blue')

tonic = get_all_with_keyword('tonic')
tonic = add_color(tonic, 'light blue')

mixers = soda + kool_aide + juice + mixes + milk + nectar + cream + hot_chocolate + ginger_shit + tea + soft_cider + lemonade + mello_yello + tonic + sprite + water
mixers = [ing for ing in mixers if ing not in alcohols]

others = [ing for ing in filtered if (ing not in mixers and ing not in alcohols)]

print (alcohols)
print (len(alcohols))
print (len(mixers))
print(len(others))
print(len(filtered) - len(mixers + alcohols + others))

mixers = remove_duplicates_by_id(mixers)
alcohols = remove_duplicates_by_id(alcohols)
others = remove_duplicates_by_id(others)

alcohols = add_category(alcohols, 0)
mixers = add_category(mixers, 1)
others = add_category(others, 2)

all = alcohols + mixers + others
for i in range(0, len(all)):
    all[i].update({'id': i})
final_list = list()
for item in all:
    final_list = final_list + convert_to_final(item)
for i in range(0, len(final_list)):
    final_list[i].update({'ID' : i})

base_ingredients = [{'ID' : ing['id'], 'Name' : ing['name'], 'Category' : ing['category']} for ing in all]

print(all)
print(final_list)
print (len(all))


print(len(filtered) - len(mixers + alcohols + others))

with open('classified-ingredients.json', 'w') as outfile:
    json.dump(final_list, outfile)

with open('base-ingredients.json', 'w') as basefile:
    json.dump(base_ingredients, basefile)