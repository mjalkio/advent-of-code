from year_2020.day21.allergen_assessment import (
    get_ingredients_with_no_allergens,
    get_num_occurences_of_ingredients,
)


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


def test_get_ingredients_with_no_allergens():
    assert get_ingredients_with_no_allergens(TEST_INPUT) == INGREDIENTS_WITH_NO_ALLERGENS


def test_get_num_occurences_of_ingredients():
    assert get_num_occurences_of_ingredients(TEST_INPUT, INGREDIENTS_WITH_NO_ALLERGENS) == 5
