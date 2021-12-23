from collections import namedtuple

from util import read_puzzle_input

A = "A"
B = "B"
C = "C"
D = "D"
HALLWAY_LENGTH = 11
ROOM_LOCATIONS = {
    A: 2,
    B: 4,
    C: 6,
    D: 8,
}
WALL_THICKNESS = 1
State = namedtuple("State", ["locations", "total_energy"])


def _get_initial_state(puzzle_input):
    lines = puzzle_input.split("\n")
    room_lines = lines[2:-1]
    room_depth = len(room_lines)
    locations = {}
    for i in range(len(room_lines)):
        for j in ROOM_LOCATIONS.values():
            locations[(j, i + 1)] = room_lines[i][j + WALL_THICKNESS]
    return (State(locations=locations, total_energy=0), room_depth)


def _get_move_cost(start_x, start_y, dest_x, dest_y, locations):
    return None


def _get_next_states(state, room_depth):
    # If any amphipod can move into its terminal state, make that move
    for (start_x, start_y), amphipod in state.locations.items():
        if start_y != 0:
            # We do not allow room -> room movement
            continue
        dest_x = ROOM_LOCATIONS[amphipod]
        # Prefer to settle all the way in the back of the room
        for dest_y in reversed(range(1, room_depth + 1)):
            move_cost = _get_move_cost(
                start_x=start_x,
                start_y=start_y,
                dest_x=dest_x,
                dest_y=dest_y,
                locations=state.locations,
            )
            if move_cost is not None:
                new_locations = state.locations.copy()
                del new_locations[(start_x, start_y)]
                new_locations[(dest_x, dest_y)] = amphipod
                return [
                    State(
                        locations=new_locations,
                        total_energy=state.total_energy + move_cost,
                    )
                ]

    # Otherwise make all moves that are valid
    next_states = []
    dest_y = 0
    for (start_x, start_y), amphipod in state.locations.items():
        if start_y == 0:
            # We do not allow hallway -> hallway movement
            continue

        for dest_x in range(HALLWAY_LENGTH):
            move_cost = _get_move_cost(
                start_x=start_x,
                start_y=start_y,
                dest_x=dest_x,
                dest_y=dest_y,
                locations=state.locations,
            )
            if move_cost is not None:
                new_locations = state.locations.copy()
                del new_locations[(start_x, start_y)]
                new_locations[(dest_x, dest_y)] = amphipod
                next_states.append(
                    State(
                        locations=new_locations,
                        total_energy=state.total_energy + move_cost,
                    )
                )

    return next_states


def _is_organized(state):
    for (x, y), amphipod in state.locations:
        if y == 0:
            return False
        if x != ROOM_LOCATIONS[amphipod]:
            return False

    return True


def get_minimum_energy_required(puzzle_input):
    minimum_energy = 1_000_000_000
    initial_state, room_depth = _get_initial_state(puzzle_input)
    states = [initial_state]
    while len(states) > 0:
        curr_state = states.pop()
        for next_state in _get_next_states(curr_state, room_depth):
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
