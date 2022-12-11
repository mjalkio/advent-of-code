from collections import deque
from math import prod

from util import read_puzzle_input

OLD = "old"
PROD = "*"


def get_monkey_business(puzzle_input, num_rounds=20, num_focus=2):
    monkey_inputs = puzzle_input.split("\n\n")
    monkeys = []
    for monkey_attributes in monkey_inputs:
        starting_items, operation, test, if_true, if_false = [
            attr.split(": ")[1]
            for attr in monkey_attributes.split("\n")
            if not attr.startswith("Monkey")
        ]
        monkey = {}
        monkey["items"] = deque([int(item) for item in starting_items.split(", ")])

        new, equals, left, op, right = operation.split()
        monkey["operator"] = prod if op == PROD else sum
        monkey["op_left"] = OLD if left == OLD else int(left)
        monkey["op_right"] = OLD if right == OLD else int(right)

        monkey["divisible_by"] = int(test.replace("divisible by ", ""))

        monkey["if_true"] = int(if_true.split()[-1])
        monkey["if_false"] = int(if_false.split()[-1])

        monkeys.append(monkey)
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_monkey_business(puzzle_input)}")
    print(f"Part 2: {get_monkey_business(puzzle_input)}")
