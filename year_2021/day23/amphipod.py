from collections import namedtuple

from util import read_puzzle_input

A = "A"
B = "B"
C = "C"
D = "D"
HALLWAY_LOCATIONS = {
    A: 2,
    B: 4,
    C: 6,
    D: 8,
}
WALL_THICKNESS = 1
State = namedtuple("State", ["locations", "total_energy"])


def _get_initial_state(puzzle_input):
    lines = puzzle_input.split("\n")
    hallway_lines = lines[2:-1]
    locations = {}
    for i in range(len(hallway_lines)):
        for j in HALLWAY_LOCATIONS.values():
            locations[(j, i + 1)] = hallway_lines[i][j + WALL_THICKNESS]
    return State(locations=locations, total_energy=0)


def _get_next_states(state):
    return []


def _is_organized(state):
    return False


def get_minimum_energy_required(puzzle_input):
    minimum_energy = 1_000_000_000
    states = [_get_initial_state(puzzle_input)]
    while len(states) > 0:
        curr_state = states.pop()
        for next_state in _get_next_states(curr_state):
            if curr_state.total_energy >= minimum_energy:
                continue
            elif _is_organized(curr_state):
                minimum_energy = curr_state.total_energy
            else:
                states.append(next_state)
    return minimum_energy


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_minimum_energy_required(puzzle_input)}")
    print(f"Part 2: {get_minimum_energy_required(puzzle_input)}")
