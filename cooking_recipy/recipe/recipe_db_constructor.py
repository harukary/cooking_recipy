import json
import glob
import datetime
import re
import sys

def main():
    args = sys.argv
    path = 'database/recipe/' + args[1]
    pathlist = get_pathlist(path)

    with open('settings/instruction_key.json', 'r', encoding='utf-8') as f:
        instruction_key = json.load(f)
    
    file_name = 'database/recipe_'+ args[1]
    recipedb_dict = {}
    recipedb_dict['recipes'] = {}

    try:
        with open(file_name + '.json', encoding="utf-8") as f:
            recipedb_dict = json.load(f)
    except:
        print("DB not found")
    
    dt_now = datetime.datetime.now()
    date = dt_now.strftime('%Y-%m-%d')
    recipedb_dict['date'] = date
    
    for path in pathlist:
        with open(path, encoding="utf-8") as f:
            df = json.load(f)
            df['abstract_instruction'] = extract_abs_inst(df['instructions'], instruction_key)
            key = df['publisher'] + '_' + df['title']
            if key in recipedb_dict['recipes'].keys():
                recipedb_dict['recipes'][key].update(df)
                print("update")
            else:
                recipedb_dict['recipes'][key] = df
                print('add')
    with open(file_name + '.json', 'w', encoding="utf-8") as f:
        json.dump(recipedb_dict, f, ensure_ascii=False, indent=4)
        print(file_name, "created")


def get_pathlist(path):
    pathlist = glob.glob(path + '/*.json')
    return pathlist

def extract_abs_inst(instruction_list, inst_key):
    instructions = ','.join(instruction_list)
    # print(instructions)
    keys_exist = []
    for rcp_class, keys in inst_key.items():
        for key in keys:
            places = [m.start() for m in re.finditer(key, instructions)]
            for place in places:
                keys_exist.append((place,rcp_class))
    keys_exist.sort()
    # print(keys_exist)
    seen = ['']
    keys_exist = [x[1] for x in keys_exist if x[1] != seen[len(seen)-1] and not seen.append(x[1])]
    return keys_exist

if __name__ == "__main__":
    main()