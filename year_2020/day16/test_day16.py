from year_2020.day16.ticket_translation import get_ticket_scanning_error_rate

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


def test_get_ticket_scanning_error_rate():
    assert get_ticket_scanning_error_rate(TEST_INPUT) == 71
