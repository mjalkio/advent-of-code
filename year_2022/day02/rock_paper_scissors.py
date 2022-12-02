from util import read_puzzle_input

ROCK = 1
PAPER = 2
SCISSORS = 3
OPP_CHOICE_MAP = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}
MY_CHOICE_MAP = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}


def get_score(puzzle_input):
    rounds = puzzle_input.split("\n")

    score = 0
    for rnd in rounds:
        if rnd == "":
            continue

        opp, me = rnd.split()
        opp_choice = OPP_CHOICE_MAP[opp]
        my_choice = MY_CHOICE_MAP[me]
        score += my_choice
        if (my_choice == ROCK and opp_choice == SCISSORS) or my_choice > opp_choice:
            score += 6
        elif my_choice == opp_choice:
            score += 3

    return score


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_score(puzzle_input)}")
    print(f"Part 2: {get_score(puzzle_input)}")
