# -*- coding: utf-8 -*-

from context import cooking_recipy
from cooking_recipy.RecipeDBAccessor import RecipeDBAccessor
from cooking_recipy.IngredientDBAccessor import IngredientDBAccessor

from cooking_recipy.recipe import recipe_parser, recipe_db_constructor

from cooking_recipy.ingredient import ingredient_db_constructor

# print(help(cooking_recipy))

# recipe_parser.main()

# recipe_db_constructor.main()

# recipedb_file = 'recipe_chefgohan.json'
# recipe = RecipeDBAccessor(recipedb_file)
# print(recipe.get_random())

# ingredient_db_constructor.main()

ingredientdb_file = 'ingredient.csv'
ingredient = IngredientDBAccessor(ingredientdb_file)
res, score = ingredient.get_random_substitution('＜鳥肉類＞　にわとり　［若どり・副品目］　ささみ　生')
print("result:", res)