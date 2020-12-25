import pytest

from year_2020.day25.combo_breaker import PUBLIC_KEY_SUBJECT_NUMBER, get_encryption_key, get_loop_size


def test_get_encryption_key():
    assert get_encryption_key(5764801, 17807724) == 14897079


@pytest.mark.parametrize('public_key, expected', [(17807724, 11), (5764801, 8)])
def test_get_loop_size(public_key, expected):
    assert get_loop_size(
        subject_number=PUBLIC_KEY_SUBJECT_NUMBER,
        public_key=public_key
    ) == expected
