from collections import defaultdict

PUZZLE_INPUT = "15,12,0,14,3,1"


def get_number_spoken(puzzle_input, num_turns=2020):
    starting_numbers = [int(num) for num in puzzle_input.split(",")]
    last_number_spoken = None
    times_spoken = defaultdict(list)
    for turn in range(num_turns):
        times_spoken[last_number_spoken].append(turn)

        if turn < len(starting_numbers):
            last_number_spoken = starting_numbers[turn]
        elif len(times_spoken[last_number_spoken]) == 1:
            last_number_spoken = 0
        else:
            last_number_times_spoken = times_spoken[last_number_spoken]
            last_number_spoken = (
                last_number_times_spoken[-1] - last_number_times_spoken[-2]
            )

    return last_number_spoken


if __name__ == "__main__":
    print(f"Part 1: {get_number_spoken(PUZZLE_INPUT)}")
    print(f"Part 2: {get_number_spoken(PUZZLE_INPUT, num_turns=30000000)}")
