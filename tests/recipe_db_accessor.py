# -*- coding: utf-8 -*-

from context import recipy
from recipy.RecipeDBAccessor import RecipeDBAccessor

# print(help(recipy))
recipedb_path = 'recipe_chefgohan.json'
recipe = RecipeDBAccessor(recipedb_path)
print(recipe.get_random())