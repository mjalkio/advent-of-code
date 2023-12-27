from util import read_puzzle_input


LEFT = "L"
RIGHT = "R"

END = "ZZZ"
START = "AAA"


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


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_steps(puzzle_input)}")
    print(f"Part 2: {get_num_steps(puzzle_input)}")
