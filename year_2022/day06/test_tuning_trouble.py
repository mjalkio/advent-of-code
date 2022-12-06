import pytest

from year_2022.day06.tuning_trouble import (
    get_first_market_idx,
)


@pytest.mark.parametrize(
    "datastream,idx",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_get_first_market_idx(datastream, idx):
    assert get_first_market_idx(datastream) == idx
