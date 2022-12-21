from collections import namedtuple

from util import read_puzzle_input


Operation = namedtuple("Operation", ["left", "operator", "right"])


ROOT = "root"
HUMAN = "humn"


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
    number_monkeys = {}
    operation_monkeys = {}
    human_operations = {}
    for line in puzzle_input.strip().split("\n"):
        monkey, job = line.split(": ")

        if monkey == HUMAN:
            continue
        elif job.isdecimal():
            number_monkeys[monkey] = int(job)
        else:
            left = job[:4]
            operator = job[5]
            if monkey == ROOT:
                operator = "=="
            right = job[7:]
            operation_monkeys[monkey] = Operation(
                left=left, operator=operator, right=right
            )

    while len(operation_monkeys) > 0:
        can_reduce = False
        for monkey, (left, operator, right) in operation_monkeys.items():
            if left in number_monkeys and right in number_monkeys:
                can_reduce = True
                break

        if not can_reduce:
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

    while len(operation_monkeys) > 0:
        for monkey, (left, operator, right) in operation_monkeys.items():
            if left in number_monkeys and right == HUMAN:
                human_operations[monkey] = f"{number_monkeys[left]} {operator} {HUMAN}"
                break
            if left == HUMAN and right in number_monkeys:
                human_operations[monkey] = f"{HUMAN} {operator} {number_monkeys[right]}"
                break
            if left in number_monkeys and right in human_operations:
                human_operations[
                    monkey
                ] = f"{number_monkeys[left]} {operator} ({human_operations[right]})"
                break
            if left in human_operations and right in human_operations:
                human_operations[
                    monkey
                ] = f"({human_operations[left]}) {operator} {number_monkeys[right]}"
                break
            if left in human_operations and right in human_operations:
                human_operations[
                    monkey
                ] = f"({human_operations[left]}) {operator} ({human_operations[right]})"
                break
            if left in human_operations and right in number_monkeys:
                human_operations[
                    monkey
                ] = f"({human_operations[left]}) {operator} {number_monkeys[right]}"
                break
            if left in number_monkeys and right in human_operations:
                human_operations[
                    monkey
                ] = f"({number_monkeys[left]}) {operator} ({human_operations[right]})"
                break

        del operation_monkeys[monkey]

    print(f"Good luck solving this:\n{human_operations[ROOT]}")
    abs_humn = 0
    while True:
        for humn in [abs_humn, abs_humn * -1]:
            if eval(human_operations[ROOT]):
                return humn
        abs_humn += 1


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {root_number(puzzle_input)}")
    print(f"Part 2: {human_number(puzzle_input)}")
