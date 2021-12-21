from util import read_puzzle_input


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
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_losing_score_times_num_rolls(puzzle_input)}")
    print(f"Part 2: {get_num_universes(puzzle_input)}")
