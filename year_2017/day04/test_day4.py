from .day4part1 import is_valid_passphrase, num_valid_passphrases
from .day4part2 import is_valid_anagram_passphrase

PART1_TEST_CASES = (
    ('aa bb cc dd ee', True),
    ('aa bb cc dd aa', False),
    ('aa bb cc dd aaa', True),
)

PART2_TEST_CASES = (
    ('abcde fghij', True),
    ('abcde xyz ecdab', False),
    ('a ab abc abd abf abj', True),
    ('iiii oiii ooii oooi oooo', True),
    ('oiii ioii iioi iiio', False),
)


def test_is_valid_passphrase():
    for passphrase, expected in PART1_TEST_CASES:
        assert is_valid_passphrase(passphrase) == expected


def test_part1():
    passphrases = '\n'.join([test_case[0] for test_case in PART1_TEST_CASES])
    num_valid = sum([test_case[1] for test_case in PART1_TEST_CASES])
    assert num_valid_passphrases(passphrases, is_valid_passphrase) == num_valid


def test_is_valid_anagram_passphrase():
    for phrase, expected in PART2_TEST_CASES:
        assert is_valid_anagram_passphrase(phrase) == expected


def test_part2():
    passphrases = '\n'.join([test_case[0] for test_case in PART2_TEST_CASES])
    num_valid = sum([test_case[1] for test_case in PART2_TEST_CASES])
    assert num_valid_passphrases(passphrases,
                                 is_valid_anagram_passphrase) == num_valid
