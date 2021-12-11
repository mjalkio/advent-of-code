from year_2020.day01.expense_report import (
    sum_two_to_2020_product,
    sum_three_to_2020_product,
)


def test_sum_to_2020_product():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    assert sum_two_to_2020_product(expense_report) == 514579


def test_sum_three_to_2020_product():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    assert sum_three_to_2020_product(expense_report) == 241861950
