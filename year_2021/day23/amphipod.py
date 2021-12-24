import heapq
from collections import namedtuple

from util import manhattan_distance, read_puzzle_input

ENERGY_COST = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}
HALLWAY_LENGTH = 11
ROOM_LOCATIONS = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}
WALL_THICKNESS = 1
State = namedtuple("State", ["total_energy", "heap_tiebreaker", "locations"])


def _counter():
    i = 0
    while True:
        yield i
        i += 1


tiebreaker = _counter()


def _get_initial_state(puzzle_input):
    lines = puzzle_input.split("\n")
    room_lines = lines[2:-1]
    room_depth = len(room_lines)
    locations = {}
    for i in range(len(room_lines)):
        for j in ROOM_LOCATIONS.values():
            locations[(j, i + 1)] = room_lines[i][j + WALL_THICKNESS]
    return (
        State(locations=locations, total_energy=0, heap_tiebreaker=next(tiebreaker)),
        room_depth,
    )


def _get_move_cost(
    start_x, start_y, dest_x, dest_y, locations, amphipod_type, room_depth
):
    if start_y == 0 and dest_y == 0:
        raise ValueError("Can't move hallway to hallway.")
    if start_y != 0 and dest_y != 0:
        raise ValueError("Can't move room to room.")

    if start_x == dest_x and start_y == dest_y:
        # Can't move to your own location
        return None

    # Don't move if you're already in the correct spot
    if start_x == ROOM_LOCATIONS[amphipod_type]:
        # Can't be blocking something else from moving
        if all(
            locations.get((start_x, y)) == amphipod_type
            for y in range(start_y + 1, room_depth + 1)
        ):
            return None

    if dest_y == 0:
        # Moving into the hallway
        if dest_x in ROOM_LOCATIONS.values():
            # Can't move to hallway outside of room
            return None

        min_x = min(start_x, dest_x)
        max_x = max(start_x, dest_x)
        for x in range(min_x, max_x + 1):
            if locations.get((x, 0)) is not None:
                return None

        for y in range(start_y):
            if locations.get((start_x, y)) is not None:
                return None
        return (
            manhattan_distance((start_x, start_y), (dest_x, dest_y))
            * ENERGY_COST[amphipod_type]
        )

    # Moving into a room
    min_x = min(start_x, dest_x)
    max_x = max(start_x, dest_x)
    for x in range(min_x + 1, max_x):
        if locations.get((x, 0)) is not None:
            return None

    for y in range(dest_y + 1):
        if locations.get((dest_x, y)) is not None:
            return None

    if dest_y < room_depth:
        for y in range(dest_y + 1, room_depth + 1):
            if locations.get((dest_x, y)) != amphipod_type:
                return None

    return (
        manhattan_distance((start_x, start_y), (dest_x, dest_y))
        * ENERGY_COST[amphipod_type]
    )


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
                amphipod_type=amphipod,
                room_depth=room_depth,
            )
            if move_cost is not None:
                new_locations = state.locations.copy()
                del new_locations[(start_x, start_y)]
                new_locations[(dest_x, dest_y)] = amphipod
                return [
                    State(
                        locations=new_locations,
                        total_energy=state.total_energy + move_cost,
                        heap_tiebreaker=next(tiebreaker),
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
                amphipod_type=amphipod,
                room_depth=room_depth,
            )
            if move_cost is not None:
                new_locations = state.locations.copy()
                del new_locations[(start_x, start_y)]
                new_locations[(dest_x, dest_y)] = amphipod
                next_states.append(
                    State(
                        locations=new_locations,
                        total_energy=state.total_energy + move_cost,
                        heap_tiebreaker=next(tiebreaker),
                    )
                )
    return next_states


def _is_organized(state):
    for (x, y), amphipod in state.locations.items():
        if y == 0:
            return False
        if x != ROOM_LOCATIONS[amphipod]:
            return False

    return True


def _print_diagram(locations, room_depth):
    hallway = ""
    for x in range(HALLWAY_LENGTH):
        hallway += locations.get((x, 0), ".")
    print(hallway)
    for y in range(1, room_depth + 1):
        room_line = ""
        for x in range(HALLWAY_LENGTH):
            if x in ROOM_LOCATIONS.values():
                room_line += locations.get((x, y), ".")
            else:
                room_line += "#"
        print(room_line)


def get_minimum_energy_required(puzzle_input):
    minimum_energy = 1_000_000_000
    initial_state, room_depth = _get_initial_state(puzzle_input)
    states = [initial_state]
    while len(states) > 0:
        curr_state = heapq.heappop(states)
        potential_next_states = _get_next_states(curr_state, room_depth)
        for next_state in potential_next_states:
            if next_state.total_energy >= minimum_energy:
                continue
            elif _is_organized(next_state):
                minimum_energy = next_state.total_energy
            else:
                heapq.heappush(states, next_state)
    return minimum_energy


if __name__ == "__main__":
    print(f"Part 1: {get_minimum_energy_required(read_puzzle_input())}")
    print(
        f"Part 2: {get_minimum_energy_required(read_puzzle_input('puzzle_input_2.txt'))}"
    )
