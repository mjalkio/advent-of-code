import json

from util import read_puzzle_input


def _snailfish_dump(number):
    return json.dumps(number, separators=(",", ":"))


def snailfish_magnitude(number):
    def _magnitude(number):
        if type(number) == int:
            return number

        left = _magnitude(number[0])
        right = _magnitude(number[1])
        return 3 * left + 2 * right

    number = json.loads(number)
    return _magnitude(number)


def snailfish_sum(puzzle_input):
    return "[0,0]"


def snailfish_add(number_a, number_b, reduce_result=True):
    return "[0,0]"


def snailfish_reduce(number):
    return "[0,0]"


def do_homework(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {do_homework(puzzle_input)}")
    print(f"Part 2: {do_homework(puzzle_input)}")
