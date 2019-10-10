#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    # create a list for no of batches
    batch = []
    # loop through the ingredient and recipe lists
    for k, v in recipe.items():
        # if an item in recipe is not availble in ingredients, return 0
        if k not in ingredients:
            return 0
        for key, val in ingredients.items():
            if k == key:
                # check if same item value in ingredients is larger than the item in recipe
                if v > val:
                    # if not return 0
                    return 0

                else:
                    # else divide the ingredient value to get how many batches you can make with the recipe
                    # and append to the batch list
                    batch.append(val // v)
    # return the minimum value in the batch list
    return min(batch)


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}."
        .format(batches=recipe_batches(recipe, ingredients),
                ingredients=ingredients))
