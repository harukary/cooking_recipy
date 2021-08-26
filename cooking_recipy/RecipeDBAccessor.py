import json
import random

class RecipeDBAccessor:
    def __init__(self,file):
        self.df = json.load(open('database/'+file, 'r', encoding='utf-8'))
    def get_random(self):
        id = random.randint(0,len(self.df['recipes'])-1)
        one_recipe = self.df['recipes'][list(self.df['recipes'].keys())[id]]
        # try:
        #     file =io.BytesIO(urlopen(one_recipe['image']).read())
        #     img = Image.open(file)
        #     im_list = np.asarray(img)
        #     plt.axis("off")
        #     plt.imshow(im_list)
        #     plt.show()
        # except:
        #     print('File not found.')
        return one_recipe
        
    def filter(self, publisher=None, max_time=None, cuisine=None, method=None):
        def match_conditions(x):
            ok = True
            # print(x)
            if publisher is not None:
                ok = (x['publisher'] == publisher)
            if max_time is not None:
                ok = (int(x['time']) <= max_time)
            if cuisine is not None:
                ok = (x['cuisine'] == cuisine)
            if method is not None:
                ok = (x['method'] == method)
            return ok
            # if ingredients is not None:
            #     okk = False
            #     for i in ingredients:
            #         for j in x['ingredients']:
            #             if i == j['mext']:
            #                 okk = True
            #     ok = okk 
        
        return list(filter(match_conditions, self.df['recipes'].values()))