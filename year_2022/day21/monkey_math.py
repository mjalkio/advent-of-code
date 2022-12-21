from collections import namedtuple

from util import read_puzzle_input


Operation = namedtuple("Operation", ["left", "operator", "right"])


ROOT = "root"


def root_number(puzzle_input):
    number_monkeys = {}
    operation_monkeys = {}
    for line in puzzle_input.strip().split("\n"):
        monkey, job = line.split(": ")
        if job.isdecimal():
            number_monkeys[monkey] = int(job)
        else:
            left = job[:4]
            operator = job[5]
            right = job[7:]
            operation_monkeys[monkey] = Operation(
                left=left, operator=operator, right=right
            )

    while len(operation_monkeys) > 0:
        for monkey, (left, operator, right) in operation_monkeys.items():
            if left in number_monkeys and right in number_monkeys:
                break
        del operation_monkeys[monkey]

        if operator == "+":
            number_monkeys[monkey] = number_monkeys[left] + number_monkeys[right]
        elif operator == "-":
            number_monkeys[monkey] = number_monkeys[left] - number_monkeys[right]
        elif operator == "/":
            number_monkeys[monkey] = number_monkeys[left] // number_monkeys[right]
        elif operator == "*":
            number_monkeys[monkey] = number_monkeys[left] * number_monkeys[right]
    return number_monkeys[ROOT]


def human_number(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {root_number(puzzle_input)}")
    print(f"Part 2: {human_number(puzzle_input)}")
