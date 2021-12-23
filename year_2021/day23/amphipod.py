from util import read_puzzle_input


def _get_initial_state(puzzle_input):
    return None


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
            if _is_organized(curr_state):
                minimum_energy = min(minimum_energy, curr_state.total_energy)
            else:
                states.append(next_state)
    return minimum_energy


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_minimum_energy_required(puzzle_input)}")
    print(f"Part 2: {get_minimum_energy_required(puzzle_input)}")
