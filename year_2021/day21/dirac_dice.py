import itertools
from collections import defaultdict, namedtuple

from util import read_puzzle_input


State = namedtuple("State", ["p1_pos", "p2_pos", "p1_score", "p2_score", "is_p1_move"])


def get_losing_score_times_num_rolls(puzzle_input):
    p1_info, p2_info = puzzle_input.split("\n")
    p1_pos = int(p1_info.replace("Player 1 starting position: ", ""))
    p2_pos = int(p2_info.replace("Player 2 starting position: ", ""))
    p1_score = 0
    p2_score = 0
    num_rolls = 0
    next_roll = 1
    is_p1_move = True
    while p1_score < 1000 and p2_score < 1000:
        if is_p1_move:
            for _ in range(3):
                p1_pos += next_roll
                while p1_pos > 10:
                    p1_pos -= 10
                next_roll += 1
                if next_roll > 100:
                    next_roll = 1

                num_rolls += 1
            p1_score += p1_pos
            is_p1_move = False
        else:
            for _ in range(3):
                p2_pos += next_roll
                while p2_pos > 10:
                    p2_pos -= 10

                next_roll += 1
                if next_roll > 100:
                    next_roll = 1

                num_rolls += 1
            p2_score += p2_pos
            is_p1_move = True
    return min(p1_score, p2_score) * num_rolls


def get_num_universes(puzzle_input):
    p1_info, p2_info = puzzle_input.split("\n")
    p1_pos = int(p1_info.replace("Player 1 starting position: ", ""))
    p2_pos = int(p2_info.replace("Player 2 starting position: ", ""))
    initial_state = State(
        p1_pos=p1_pos,
        p2_pos=p2_pos,
        p1_score=0,
        p2_score=0,
        is_p1_move=True,
    )

    state_counts = defaultdict(int)
    state_counts[initial_state] += 1
    move_possibilities = itertools.product([1, 2, 3], repeat=3)
    roll_sum_counts = defaultdict(int)
    for combo in move_possibilities:
        roll_sum_counts[sum(combo)] += 1

    p1_wins = 0
    p2_wins = 0
    while len(state_counts) > 0:
        state, num_universes = state_counts.popitem()
        if state.p1_score > 21:
            p1_wins += num_universes
            continue
        if state.p2_score > 21:
            p2_wins += num_universes
            continue

        if state.is_p1_move:
            for steps_forward, num_new_universes in roll_sum_counts.items():
                new_p1_pos = state.p1_pos + steps_forward
                if new_p1_pos > 10:
                    new_p1_pos -= 10

                new_state = State(
                    p1_pos=new_p1_pos,
                    p2_pos=state.p2_pos,
                    p1_score=state.p1_score + new_p1_pos,
                    p2_score=state.p2_score,
                    is_p1_move=False,
                )
                state_counts[new_state] += num_new_universes * num_universes
        else:
            for steps_forward, num_new_universes in roll_sum_counts.items():
                new_p2_pos = state.p2_pos + steps_forward
                if new_p2_pos > 10:
                    new_p2_pos -= 10

                new_state = State(
                    p1_pos=state.p1_pos,
                    p2_pos=new_p2_pos,
                    p1_score=state.p1_score,
                    p2_score=state.p2_score + new_p2_pos,
                    is_p1_move=True,
                )
                state_counts[new_state] += num_new_universes * num_universes
    return max(p1_wins, p2_wins)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_losing_score_times_num_rolls(puzzle_input)}")
    print(f"Part 2: {get_num_universes(puzzle_input)}")
