#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = 0
  still_cooking = True
  while still_cooking:
    ingredients_added = 0
    for item in recipe.items():
      if item[0] not in ingredients:
        still_cooking = False
      elif ingredients[item[0]] < item[1]:
        still_cooking = False
      else:
        ingredients[item[0]] -= item[1]
        ingredients_added += 1
        if ingredients_added == len(recipe.keys()):
           batches += 1
  return batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))