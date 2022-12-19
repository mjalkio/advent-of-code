from collections import namedtuple

from util import read_puzzle_input


Minerals = namedtuple(
    "Minerals", ["ore", "clay", "obsidian", "geode"], defaults=[0, 0, 0, 0]
)
State = namedtuple("State", ["minute", "ore_counts", "robot_counts"])


TIME_LIMIT = 24


def _can_build(robot_idx, minute, robot_counts, robot_costs):
    return False


def sum_quality_levels(puzzle_input):
    quality_level_sum = 0

    for blueprint in puzzle_input.strip().split("\n"):
        most_geodes_produced = 0
        words = blueprint.split()
        blueprint_idx = int(words[1][:-1])
        ore_robot_cost = Minerals(ore=int(words[6]))
        clay_robot_cost = Minerals(ore=int(words[12]))
        obsidian_robot_cost = Minerals(ore=int(words[18]), clay=int(words[21]))
        geode_robot_cost = Minerals(ore=int(words[27]), obsidian=int(words[30]))
        robot_costs = Minerals(
            ore=ore_robot_cost,
            clay=clay_robot_cost,
            obsidian=obsidian_robot_cost,
            geode=geode_robot_cost,
        )

        stack = [State(minute=1, ore_counts=Minerals(), robot_counts=Minerals(ore=1))]
        while len(stack) > 0:
            minute, ore_counts, robot_counts = stack.pop()
            can_build_more = False
            for robot_idx in range(len(robot_costs)):
                if _can_build(
                    robot_idx=robot_idx,
                    minute=minute,
                    robot_counts=robot_counts,
                    robot_costs=robot_costs,
                ):
                    can_build_more = True

            if not can_build_more:
                geodes_produced = ore_counts.geode
                geodes_produced += robot_counts.geode * (TIME_LIMIT - minute)
                most_geodes_produced = max(geodes_produced, most_geodes_produced)
        quality_level_sum += blueprint_idx * most_geodes_produced
    return quality_level_sum


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_quality_levels(puzzle_input)}")
    print(f"Part 2: {sum_quality_levels(puzzle_input)}")
