from util import read_puzzle_input


def get_ingredients_with_no_allergens(puzzle_input):
    return None


def get_num_occurences_of_ingredients(puzzle_input, ingredients):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    ingredients_with_no_allergens = get_ingredients_with_no_allergens(puzzle_input)
    ingredients_with_no_allergens_count = get_num_occurences_of_ingredients(
        puzzle_input=puzzle_input,
        ingredients=ingredients_with_no_allergens,
    )

    print(f"Part 1: {ingredients_with_no_allergens_count}")
    print(f"Part 2: {None}")
