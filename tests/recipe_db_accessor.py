# -*- coding: utf-8 -*-

from context import cooking_recipy
from cooking_recipy.RecipeDBAccessor import RecipeDBAccessor

# print(help(cooking_recipy))
recipedb_path = 'recipe_chefgohan.json'
recipe = RecipeDBAccessor(recipedb_path)
print(recipe.get_random())