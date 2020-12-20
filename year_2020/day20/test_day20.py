from year_2020.day20.jurassic_jigsaw import get_corner_ids_product

from util import read_puzzle_input

TEST_INPUT = read_puzzle_input('test_input.txt')


def test_get_corner_ids_product():
    assert get_corner_ids_product(TEST_INPUT) == 20899048083289
