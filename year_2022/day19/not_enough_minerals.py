import math
from collections import namedtuple

from util import read_puzzle_input


Minerals = namedtuple(
    "Minerals", ["ore", "clay", "obsidian", "geode"], defaults=[0, 0, 0, 0]
)
GEODE_IDX = 3
State = namedtuple("State", ["minute", "ore_counts", "robot_counts"])


TIME_LIMIT_PART_1 = 24
TIME_LIMIT_PART_2 = 32


def _add(a, b):
    return Minerals(a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])


def _sub(a, b):
    return Minerals(a[0] - b[0], a[1] - b[1], a[2] - b[2], a[3] - b[3])


def _increment(minerals, idx):
    minerals_list = list(minerals)
    minerals_list[idx] += 1
    return Minerals._make(minerals_list)


def _greater_than(a, b):
    return any(a[i] > b[i] for i in range(len(a)))


def _next_states(state, robot_costs, time_limit):
    minute, ore_counts, robot_counts = state
    next_states = []

    for robot_idx in range(len(robot_costs)):
        cost = robot_costs[robot_idx]
        if any(cost[i] > 0 and robot_counts[i] == 0 for i in range(len(cost))):
            # We aren't producing required materials for this robot
            # TODO: We can avoid calculating this every time
            continue

        # Do we want to produce more of this robot? Will we be able to use the material?
        max_needed = max(cost[robot_idx] for cost in robot_costs)
        if robot_counts[robot_idx] >= max_needed and robot_idx != GEODE_IDX:
            continue

        # We need to have enough time
        new_minute = minute
        new_ore_counts = ore_counts
        while new_minute < time_limit and _greater_than(cost, new_ore_counts):
            # TODO: Can be sped up
            # calculate number of steps needed instead of going one at a time
            new_minute += 1
            new_ore_counts = _add(new_ore_counts, robot_counts)

        if new_minute != time_limit:
            new_ore_counts = _sub(new_ore_counts, cost)
            new_ore_counts = _add(new_ore_counts, robot_counts)
            new_robot_counts = _increment(robot_counts, robot_idx)
            next_states.append(
                State(
                    minute=new_minute + 1,
                    ore_counts=new_ore_counts,
                    robot_counts=new_robot_counts,
                )
            )

    return next_states


def _get_most_geodes_produced(blueprint, time_limit):
    most_geodes_produced = 0
    words = blueprint.split()
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

    stack = [State(minute=0, ore_counts=Minerals(), robot_counts=Minerals(ore=1))]
    while len(stack) > 0:
        state = stack.pop()
        next_states = _next_states(state, robot_costs, time_limit)

        if len(next_states) == 0:
            # We can't build more robots from this state
            geodes_produced = state.ore_counts.geode
            geodes_produced += state.robot_counts.geode * (time_limit - state.minute)
            most_geodes_produced = max(geodes_produced, most_geodes_produced)
        stack += next_states
    return most_geodes_produced


def sum_quality_levels(puzzle_input):
    quality_level_sum = 0

    for i, blueprint in enumerate(puzzle_input.strip().split("\n")):
        most_geodes_produced = _get_most_geodes_produced(
            blueprint, time_limit=TIME_LIMIT_PART_1
        )
        quality_level_sum += (i + 1) * most_geodes_produced
    return quality_level_sum


def geode_count_product(puzzle_input):
    blueprints = puzzle_input.strip().split("\n")[:3]
    return math.prod(
        _get_most_geodes_produced(blueprint, time_limit=TIME_LIMIT_PART_2)
        for blueprint in blueprints
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_quality_levels(puzzle_input)}")
    print(f"Part 2: {geode_count_product(puzzle_input)}")
