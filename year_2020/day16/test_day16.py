from year_2020.day16.ticket_translation import (
    get_field_order,
    get_ticket_scanning_error_rate,
)

TEST_INPUT = """
class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
"""

TEST_INPUT_2 = """
class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
"""


def test_get_ticket_scanning_error_rate():
    assert get_ticket_scanning_error_rate(TEST_INPUT) == 71


def test_get_field_order():
    assert get_field_order(TEST_INPUT_2) == ['row', 'class', 'seat']
