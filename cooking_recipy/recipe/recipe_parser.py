from urllib import request 
from bs4 import BeautifulSoup
import json
import time
import sys

target_list = ['chefgohan', 'luttuceclub', 'orangepage', 'kurashiru', None]

def main():
    args = sys.argv
    setting_file = 'settings/' + args[1]
    setting = 'setting/parser.json'
    try:
        with open(setting_file, 'r') as f:
            setting = json.load(f)
    except:
        print('Error! Setting file not found:', setting_file)
        return
    target = setting['target']
    s = setting['id_start']
    e = setting['id_end']
    if target not in target_list:
        return
    id_list = [i for i in range(s,e)]
    print(target, ':',s,'to',e )
    if target=='chefgohan':
        for id in id_list:
            parse_chefgohan(id)
            time.sleep(1)
    elif target=='luttuceclub':
        print('Not supported yet')
    elif target=='orangepage':
        print('Not supported yet')
    elif target=='kurashiru':
        print('Not supported yet')
    else:
        print('Not supported')

def parse_chefgohan(id):
    url = 'https://chefgohan.gnavi.co.jp/detail/' + str(id) + '/'
    response = request.urlopen(url)
    soup = BeautifulSoup(response, features="html.parser")
    response.close()
    ok = soup.find('script', type='application/ld+json')
    if ok is None:
        print(id,':',url,"...URL not exist")
        return
    txt_chef = ok.string
    json_chef = json.loads(txt_chef)
    # print([{'name': i.split(':')[0].split('\u3000')[0], 'quantity': i.split(':')[1]} for i in json_chef['recipeIngredient']])
    # print([inst.split('.')[1].split('\u3000')[0] for inst in json_chef['recipeInstructions']])
    # print(json_chef['recipeIngredient'])
    ingredients = []
    for i in json_chef['recipeIngredient']:
        ingr_and_q = i.split(':')
        if len(ingr_and_q) == 1:
            ingredients.append({'name': i.split(':')[0].split('\u3000')[0]})
        elif len(ingr_and_q) > 1:
            ingredients.append({'name': i.split(':')[0].split('\u3000')[0], 'quantity': i.split(':')[1]})

    json_recipe = {
        'publisher': json_chef['publisher']['name'],
        'title': json_chef['name'].replace('\t',''),
        'image': json_chef['image'],
        'date': json_chef['datePublished'].split(' ')[0],
        'time': json_chef['totalTime'].replace('PT','').replace('M',''),
        'num': json_chef['recipeYield'],
        'method': json_chef['cookingMethod'],
        'cuisine': json_chef['recipeCuisine'],
        'author': json_chef['author']['name'],
        'ingredients': ingredients,
        'instructions': [inst.split('.')[1].split('\u3000')[0] for inst in json_chef['recipeInstructions']]
    }
    file_name = 'database/recipe/chefgohan/chefgohan_' + json_chef['name'].replace('\t','') + '.json'
    with open(file_name, 'w', encoding="utf-8") as f:
        json.dump(json_recipe, f, ensure_ascii=False, indent=4)
    print(id,':',url,"...Done")

def parse_lettuceclub():
    print('lettuceclub')

def parse_orangepage():
    print('orangepage')

def parse_kurashiru():
    print('kurashiru')

if __name__ == "__main__":
    main()