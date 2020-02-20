#!/usr/bin/python

import math

def recipe_batches(d1, d2):
      k1 = set(d1.keys())
      k2 = set(d2.keys())
      common_keys = set(k1).intersection(set(k2))
      current_max_rec=[]
      value = { k : d1[k] for k in set(d1) - set(d2) }
      values = bool(value)
      if values == True:
        current_max_rec.append(0)
      else:
        for key in common_keys:
          if d2[key] >= d1[key]:
              current_max_rec.append(d2[key] // d1[key])
          elif d2[key] < d1[key]:
              current_max_rec.append(0)
          

      return min(current_max_rec)
 
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 150, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))