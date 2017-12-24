from .day4part1 import is_valid_passphrase


def test_is_valid_passphrase():
    test_cases = [
        ('aa bb cc dd ee', True),
        ('aa bb cc dd aa', False),
        ('aa bb cc dd aaa', True),
    ]

    for passphrase, expected in test_cases:
        assert is_valid_passphrase(passphrase) == expected
