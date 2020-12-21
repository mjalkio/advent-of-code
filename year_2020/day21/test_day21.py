from year_2020.day21.allergen_assessment import (
    get_allergens_to_ingredients_map,
    get_canonical_dangerous_ingredient_list,
    get_ingredients_with_no_allergens,
    get_num_occurences_of_ingredients,
)


ALLERGENS_TO_INGREDIENTS = {
    'dairy': 'mxmxvkd',
    'fish': 'sqjhc',
    'soy': 'fvjkl',
}

CANONICAL_DANGEROUS_INGREDIENT_LIST = 'mxmxvkd,sqjhc,fvjkl'

TEST_INPUT = """
mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)
"""

INGREDIENTS_WITH_NO_ALLERGENS = set([
    'kfcds',
    'nhms',
    'sbzzf',
    'trh',
])


def test_get_allergens_to_ingredients_map():
    assert get_allergens_to_ingredients_map(TEST_INPUT) == ALLERGENS_TO_INGREDIENTS


def test_get_canonical_dangerous_ingredient_list():
    assert (
        get_canonical_dangerous_ingredient_list(TEST_INPUT) == CANONICAL_DANGEROUS_INGREDIENT_LIST
    )


def test_get_ingredients_with_no_allergens():
    assert get_ingredients_with_no_allergens(TEST_INPUT) == INGREDIENTS_WITH_NO_ALLERGENS


def test_get_num_occurences_of_ingredients():
    assert get_num_occurences_of_ingredients(TEST_INPUT, INGREDIENTS_WITH_NO_ALLERGENS) == 5
