import math

from util import read_puzzle_input


LEFT = "L"
RIGHT = "R"

END = "ZZZ"
START = "AAA"

END_CHAR = "Z"
START_CHAR = "A"


def get_num_steps(puzzle_input):
    lines = puzzle_input.split("\n")
    instructions = lines[0]
    node_inputs = lines[2:]
    nodes = {}
    for ni in node_inputs:
        node, connections = ni.split(" = ")
        left, right = connections[1:-1].split(", ")
        nodes[node] = {LEFT: left, RIGHT: right}

    current_node = START
    num_steps = 0
    while current_node != END:
        next_instruction = instructions[num_steps % len(instructions)]
        current_node = nodes[current_node][next_instruction]
        num_steps += 1
    return num_steps


def get_num_steps_ghost(puzzle_input):
    lines = puzzle_input.split("\n")
    instructions = lines[0]
    node_inputs = lines[2:]
    nodes = {}
    for ni in node_inputs:
        node, connections = ni.split(" = ")
        left, right = connections[1:-1].split(", ")
        nodes[node] = {LEFT: left, RIGHT: right}

    start_nodes = [n for n in nodes if n.endswith(START_CHAR)]
    steps_to_z = []
    for current_node in start_nodes:
        num_steps = 0
        while not current_node.endswith(END_CHAR):
            next_instruction = instructions[num_steps % len(instructions)]
            current_node = nodes[current_node][next_instruction]
            num_steps += 1
        steps_to_z.append(num_steps)

    return math.lcm(*steps_to_z)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_steps(puzzle_input)}")
    print(f"Part 2: {get_num_steps_ghost(puzzle_input)}")
