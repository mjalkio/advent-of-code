from util import read_puzzle_input


def _split_numbers(number_input):
    # Numbers are all between 1 and 99
    return [number_input[i : i + 3].strip() for i in range(0, len(number_input), 3)]


def get_point_value(puzzle_input):
    point_value = 0
    card_inputs = puzzle_input.split("\n")
    for card in card_inputs:
        winning_input, number_input = card.split(": ")[1].split(" | ")
        winning_numbers = _split_numbers(winning_input)
        numbers_you_have = _split_numbers(number_input)
        winners = [num for num in numbers_you_have if num in winning_numbers]
        num_wins = len(winners)
        if num_wins == 1:
            point_value += 1
        elif num_wins > 1:
            point_value += 2 ** (num_wins - 1)
        # print(f"Num wins {num_wins}, point_value {point_value}")
    return point_value


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_point_value(puzzle_input)}")
    print(f"Part 2: {get_point_value(puzzle_input)}")
