from collections import namedtuple

from util import read_puzzle_input


Minerals = namedtuple("Minerals", ["ore", "clay", "obsidian"], defaults=[0, 0, 0])


def sum_quality_levels(puzzle_input):
    # Goal is to produce geodes
    #
    # Geode robots require ore and obsidian
    # Obsidian robots require ore and clay
    # Clay robots require ore
    # Ore robots require ore
    for blueprint in puzzle_input.strip().split("\n"):
        words = blueprint.split()
        ore_robot_cost = Minerals(ore=int(words[6]))
        clay_robot_cost = Minerals(ore=int(words[12]))
        obsidian_robot_cost = Minerals(ore=int(words[18]), clay=int(words[21]))
        geode_robot_cost = Minerals(ore=int(words[27]), obsidian=int(words[30]))
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_quality_levels(puzzle_input)}")
    print(f"Part 2: {sum_quality_levels(puzzle_input)}")
