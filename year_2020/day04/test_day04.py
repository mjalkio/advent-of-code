import pytest

from year_2020.day04.passport_processing import (
    num_valid_passports,
    passport_batch_to_tuple,
    passport_is_valid,
)

TEST_INPUT_1 = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

INPUT_1 = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
INPUT_2 = 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929'
INPUT_3 = 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm'
INPUT_4 = 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in'


def test_passport_batch_to_tuple():
    assert passport_batch_to_tuple(TEST_INPUT_1) == (INPUT_1, INPUT_2, INPUT_3, INPUT_4)


@pytest.mark.parametrize(
    'passport,expected',
    [
        (INPUT_1, True),
        (INPUT_2, False),
        (INPUT_3, True),
        (INPUT_4, False),
    ]
)
def test_passport_is_valid(passport, expected):
    assert passport_is_valid(passport) == expected


def test_num_valid_passports():
    assert num_valid_passports(TEST_INPUT_1) == 2
