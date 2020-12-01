from .expense_report import sum_to_2020_product


def test_sum_to_2020_product():
    expense_report = [1721, 979, 366, 299, 675, 1456]
    assert sum_to_2020_product(expense_report) == 514579
