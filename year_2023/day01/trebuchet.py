from util import read_puzzle_input


def sum_calibration_values(puzzle_input):
    answer = 0
    for value in puzzle_input.split("\n"):
        digits = [c for c in value if c.isdigit()]
        answer += int(digits[0] + digits[-1])
    return answer


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_calibration_values(puzzle_input)}")
    print(f"Part 2: {sum_calibration_values(puzzle_input)}")
