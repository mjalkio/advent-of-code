from util import read_puzzle_input

from collections import Counter


def _parse_foods(puzzle_input):
    food_list = [line for line in puzzle_input.split('\n') if line != '']

    ingredients_and_allergens = []
    for food_line in food_list:
        ingredients_definition, allergens_definition = food_line.split(' (contains ')
        allergens = allergens_definition[:-1].split(', ')
        ingredients = ingredients_definition.split(' ')
        ingredients_and_allergens.append((ingredients, allergens))
    return ingredients_and_allergens


def get_ingredients_with_no_allergens(puzzle_input):
    ingredients_and_allergens = _parse_foods(puzzle_input)

    ingredients_possibly_containing = {}
    for ingredients, allergens in ingredients_and_allergens:
        for allergen in allergens:
            if allergen not in ingredients_possibly_containing:
                ingredients_possibly_containing[allergen] = set(ingredients)
                continue
            ingredients_possibly_containing[allergen] = (
                ingredients_possibly_containing[allergen].intersection(
                    set(ingredients)
                )
            )

    all_ingredients = set([
        ingredient
        for ingredients, _
        in ingredients_and_allergens
        for ingredient
        in ingredients
    ])
    ingredients_possibly_containing_allergens = set.union(*ingredients_possibly_containing.values())
    return all_ingredients - ingredients_possibly_containing_allergens


def get_num_occurences_of_ingredients(puzzle_input, ingredients):
    ingredients_and_allergens = _parse_foods(puzzle_input)
    ingredient_counts = Counter(
        ingredient
        for ingredients, _
        in ingredients_and_allergens
        for ingredient
        in ingredients
    )
    return sum(ingredient_counts[ingredient] for ingredient in ingredients)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    ingredients_with_no_allergens = get_ingredients_with_no_allergens(puzzle_input)
    ingredients_with_no_allergens_count = get_num_occurences_of_ingredients(
        puzzle_input=puzzle_input,
        ingredients=ingredients_with_no_allergens,
    )

    print(f"Part 1: {ingredients_with_no_allergens_count}")
    print(f"Part 2: {None}")
