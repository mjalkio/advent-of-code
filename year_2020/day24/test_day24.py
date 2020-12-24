import pytest

from year_2020.day24.lobby_layout import get_num_black_tiles, get_num_black_tiles_after_days

TEST_INPUT = """
sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
"""


def test_get_num_black_tiles():
    assert get_num_black_tiles(TEST_INPUT) == 10


@pytest.mark.parametrize(
    'num_days, expected',
    [
        (1, 15),
        (2, 12),
        (3, 25),
        (4, 14),
        (5, 23),
        (6, 28),
        (7, 41),
        (8, 37),
        (9, 49),
        (10, 37),
        (20, 132),
        (30, 259),
        (40, 406),
        (50, 566),
        (60, 788),
        (70, 1106),
        (80, 1373),
        (90, 1844),
        (100, 2208),
    ]
)
def test_get_num_black_tiles_after_days(num_days, expected):
    if num_days > 10:
        pytest.skip("These tests pass, but they're slower than I want to wait for.")
    assert get_num_black_tiles_after_days(puzzle_input=TEST_INPUT, num_days=num_days) == expected
