from util import read_puzzle_input
from year_2022.day24.blizzard_basin import (
    num_minutes_to_goal,
    num_minutes_to_goal_twice,
)


def test_num_minutes_to_goal():
    assert num_minutes_to_goal(read_puzzle_input("test_input.txt")) == 18


def test_num_minutes_to_goal_twice():
    assert num_minutes_to_goal_twice(read_puzzle_input("test_input.txt")) == 54
