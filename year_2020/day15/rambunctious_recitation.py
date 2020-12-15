PUZZLE_INPUT = "15,12,0,14,3,1"


def get_number_spoken(puzzle_input, num_turns=2020):
    starting_numbers = [int(num) for num in puzzle_input.split(',')]
    last_number_spoken = None
    for turn in range(num_turns):
        if turn < len(starting_numbers):
            last_number_spoken = starting_numbers[turn]
            continue
    return last_number_spoken


if __name__ == '__main__':
    print(f"Part 1: {get_number_spoken(PUZZLE_INPUT)}")
    print(f"Part 2: {None}")
