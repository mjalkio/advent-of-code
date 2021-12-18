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
    result = f"[{number_a},{number_b}]"
    if not reduce_result:
        return result

    reduced_result = snailfish_reduce(result)
    while reduced_result != result:
        result = reduced_result
        reduced_result = snailfish_reduce(result)
    return result


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
        comma_idx = number.find(",", i + 2)
        right_brace_idx = number.find("]", i + 2)
        left_val = int(number[i + 1 : comma_idx])
        right_val = int(number[comma_idx + 1 : right_brace_idx])

        next_left_comma_idx = number[:i].rfind(",")
        if next_left_comma_idx == -1:
            left = number[:i]
        else:
            for j in reversed(range(next_left_comma_idx)):
                if number[j - 1 : j + 1].isdigit():
                    next_left_val = int(number[j - 1 : j + 1])
                    next_left_val_start_idx = j - 1
                    break
                elif number[j].isdigit():
                    next_left_val = int(number[j])
                    next_left_val_start_idx = j
                    break
            left = (
                number[:next_left_val_start_idx]
                + f"{left_val + next_left_val}"
                + number[j + 1 : i]
            )

        next_right_comma_idx = number.find(",", right_brace_idx + 1)
        if next_right_comma_idx == -1:
            right = number[right_brace_idx + 1 :]
        else:
            for j in range(right_brace_idx + 1, len(number)):
                if number[j : j + 2].isdigit():
                    next_right_val = int(number[j : j + 2])
                    next_right_val_end_idx = j + 2
                    break
                elif number[j].isdigit():
                    next_right_val = int(number[j])
                    next_right_val_end_idx = j + 1
                    break
            right = (
                number[right_brace_idx + 1 : j]
                + f"{right_val + next_right_val}"
                + number[next_right_val_end_idx:]
            )

        return left + "0" + right

    for i, char in enumerate(number):
        if number[i : i + 2].isdigit():
            # Two digit number needs a split
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
