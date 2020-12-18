import pytest

from year_2020.day18.operation_order import evaluate_expression


@pytest.mark.parametrize(
    'expression,expected',
    [
        ('1 + 2 * 3 + 4 * 5 + 6', 71),
        ('1 + (2 * 3) + (4 * (5 + 6))', 51),
        ('2 * 3 + (4 * 5)', 26),
        ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 437),
        ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 12240),
        ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 13632),
    ]
)
def test_evaluate_expression(expression, expected):
    assert evaluate_expression(expression) == expected
