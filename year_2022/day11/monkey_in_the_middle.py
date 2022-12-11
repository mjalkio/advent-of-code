from collections import deque
from math import prod

from util import read_puzzle_input

OLD = "old"
PROD = "*"

ITEMS = "items"
OPERATOR = "operator"
OP_LEFT = "op_left"
OP_RIGHT = "op_right"
DIVISIBLE_BY = "divisible_by"
IF_TRUE = "if_true"
IF_FALSE = "if_false"
ITEMS_INSPECTED = "items_inspected"

NUM_FOCUS = 2


def get_monkey_business(puzzle_input, num_rounds=20, very_worried=False):
    monkey_inputs = puzzle_input.split("\n\n")
    monkeys = []
    for monkey_attributes in monkey_inputs:
        starting_items, operation, test, if_true, if_false = [
            attr.split(": ")[1]
            for attr in monkey_attributes.split("\n")
            if not attr.startswith("Monkey")
        ]
        monkey = {}
        monkey[ITEMS] = deque([int(item) for item in starting_items.split(", ")])

        new, equals, left, op, right = operation.split()
        monkey[OPERATOR] = prod if op == PROD else sum
        monkey[OP_LEFT] = OLD if left == OLD else int(left)
        monkey[OP_RIGHT] = OLD if right == OLD else int(right)

        monkey[DIVISIBLE_BY] = int(test.replace("divisible by ", ""))

        monkey[IF_TRUE] = int(if_true.split()[-1])
        monkey[IF_FALSE] = int(if_false.split()[-1])

        monkey[ITEMS_INSPECTED] = 0

        monkeys.append(monkey)

    for _ in range(num_rounds):
        for monkey in monkeys:
            while len(monkey[ITEMS]) > 0:
                item = monkey[ITEMS].popleft()
                monkey[ITEMS_INSPECTED] += 1
                left = item if monkey[OP_LEFT] == OLD else monkey[OP_LEFT]
                right = item if monkey[OP_RIGHT] == OLD else monkey[OP_RIGHT]
                item = monkey[OPERATOR]([left, right])
                if not very_worried:
                    item //= 3

                if item % monkey[DIVISIBLE_BY] == 0:
                    monkeys[monkey[IF_TRUE]][ITEMS].append(item)
                else:
                    monkeys[monkey[IF_FALSE]][ITEMS].append(item)

    inspection_nums = sorted([m[ITEMS_INSPECTED] for m in monkeys])
    return prod(inspection_nums[-NUM_FOCUS:])


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_monkey_business(puzzle_input)}")
    print(
        f"Part 2: {get_monkey_business(puzzle_input, num_rounds=10_000, very_worried=True)}"
    )
