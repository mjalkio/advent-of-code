from util import read_puzzle_input
from year_2022.day07.no_space_left_on_device import (
    get_directory_to_delete_size,
    sum_total_size_small_directories,
)


def test_sum_total_size_small_directories():
    assert (
        sum_total_size_small_directories(read_puzzle_input("test_input.txt")) == 95437
    )


def test_get_directory_to_delete_size():
    assert get_directory_to_delete_size(read_puzzle_input("test_input.txt")) == 24933642
