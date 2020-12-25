from year_2020.day25.combo_breaker import get_encryption_key


def test_get_encryption_key():
    assert get_encryption_key(5764801, 17807724) == 14897079
