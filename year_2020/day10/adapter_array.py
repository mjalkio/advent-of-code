from collections import defaultdict

from util import read_puzzle_input


def _parse_input(puzzle_input):
    return [int(line) for line in puzzle_input.split("\n") if line != ""]


def get_joltage_difference_counts(
    puzzle_input,
    charging_outlet_joltage=0,
    allowed_differences=(1, 2, 3),
    device_joltage_difference=3,
):
    adapters = _parse_input(puzzle_input)
    adapters.sort()
    adapters.append(adapters[-1] + device_joltage_difference)

    joltage_differences = defaultdict(int)
    curr_joltage = charging_outlet_joltage
    for adapter_joltage in adapters:
        joltage_diff = adapter_joltage - curr_joltage
        if joltage_diff not in allowed_differences:
            raise ValueError("What are you doing step joltage?")
        joltage_differences[joltage_diff] += 1
        curr_joltage = adapter_joltage

    return tuple(joltage_differences[diff] for diff in allowed_differences)


def get_num_ways_to_arrange_adapters(
    puzzle_input,
    charging_outlet_joltage=0,
    device_joltage_difference=3,
    max_joltage_diff=3,
):
    adapters = _parse_input(puzzle_input)
    adapters.append(0)
    adapters.sort()
    adapters.append(adapters[-1] + device_joltage_difference)

    next_adapter_options = {}
    for i, joltage in enumerate(adapters):
        next_adapter_options[joltage] = [
            adapters[j]
            for j in range(i + 1, min(i + 4, len(adapters)))
            if adapters[j] - joltage <= max_joltage_diff
        ]

    adapters.sort(reverse=True)
    num_options_from_here = {}
    for joltage in adapters:
        if len(next_adapter_options[joltage]) == 0:
            num_options_from_here[joltage] = 1
            continue

        num_options_from_here[joltage] = sum(
            num_options_from_here[next_joltage]
            for next_joltage in next_adapter_options[joltage]
        )
    return num_options_from_here[0]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    part_1_differences = get_joltage_difference_counts(puzzle_input)
    print(f"Part 1: {part_1_differences[0] * part_1_differences[2]}")
    print(f"Part 2: {get_num_ways_to_arrange_adapters(puzzle_input)}")
