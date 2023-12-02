from util import read_puzzle_input


DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def _get_digit(value, idx):
    if value[idx].isdigit():
        return value[idx]
    for length in [3, 4, 5]:
        if value[idx : idx + length] in DIGITS:
            return DIGITS[value[idx : idx + length]]


def sum_calibration_values(puzzle_input, parse_words=False):
    answer = 0
    for value in puzzle_input.split("\n"):
        if parse_words:
            digits = [
                _get_digit(value, i) for i in range(len(value)) if _get_digit(value, i)
            ]
        else:
            digits = [c for c in value if c.isdigit()]
        answer += int(digits[0] + digits[-1])
    return answer


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_calibration_values(puzzle_input)}")
    print(f"Part 2: {sum_calibration_values(puzzle_input, parse_words=True)}")
