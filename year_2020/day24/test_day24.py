import pytest

from year_2020.day24.lobby_layout import (
    get_num_black_tiles,
    get_num_black_tiles_after_days,
)

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
    "num_days, expected",
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
        pytest.param(20, 132, marks=pytest.mark.slow),
        pytest.param(30, 259, marks=pytest.mark.slow),
        pytest.param(40, 406, marks=pytest.mark.slow),
        pytest.param(50, 566, marks=pytest.mark.slow),
        pytest.param(60, 788, marks=pytest.mark.slow),
        pytest.param(70, 1106, marks=pytest.mark.slow),
        pytest.param(80, 1373, marks=pytest.mark.slow),
        pytest.param(90, 1844, marks=pytest.mark.slow),
        pytest.param(100, 2208, marks=pytest.mark.slow),
    ],
)
def test_get_num_black_tiles_after_days(num_days, expected):
    assert (
        get_num_black_tiles_after_days(puzzle_input=TEST_INPUT, num_days=num_days)
        == expected
    )
