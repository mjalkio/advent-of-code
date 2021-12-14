PUZZLE_INPUT = "15,12,0,14,3,1"


def get_number_spoken(puzzle_input, num_turns=2020):
    starting_numbers = [int(num) for num in puzzle_input.split(",")]
    if num_turns <= len(starting_numbers):
        return starting_numbers[num_turns - 1]

    last_number_spoken = starting_numbers[-1]
    times_spoken = {
        starting_numbers[i]: (i + 1, i + 1) for i in range(len(starting_numbers) - 1)
    }
    for turn in range(len(starting_numbers), num_turns):
        if last_number_spoken not in times_spoken:
            times_spoken[last_number_spoken] = (turn, turn)
        else:
            last_last_time_spoken = times_spoken[last_number_spoken][0]
            times_spoken[last_number_spoken] = (turn, last_last_time_spoken)

        last_time_spoken, last_last_time_spoken = times_spoken[last_number_spoken]
        last_number_spoken = last_time_spoken - last_last_time_spoken

    return last_number_spoken


if __name__ == "__main__":
    print(f"Part 1: {get_number_spoken(PUZZLE_INPUT)}")
    print(f"Part 2: {get_number_spoken(PUZZLE_INPUT, num_turns=30_000_000)}")
