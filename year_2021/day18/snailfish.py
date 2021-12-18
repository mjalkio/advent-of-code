import json
import math

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
    # Assumption: Number being passed in to reduction does not have
    # anything with > 5 levels of nesting.
    nesting_amount = 0
    for i, char in enumerate(number):
        if char == "[":
            nesting_amount += 1
            if nesting_amount == 5:
                break
        if char == "]":
            nesting_amount -= 1

    if nesting_amount == 5:
        # Explode
        return "[0,0]"

    for i, char in enumerate(number):
        if number[i : i + 2].isdigit():
            # Two digit number needs it needs a split
            split_num = int(number[i : i + 2])
            left = math.floor(split_num / 2)
            right = math.ceil(split_num / 2)
            return number[:i] + f"[{left},{right}]" + number[i + 2 :]
    return number


def do_homework(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {do_homework(puzzle_input)}")
    print(f"Part 2: {do_homework(puzzle_input)}")
