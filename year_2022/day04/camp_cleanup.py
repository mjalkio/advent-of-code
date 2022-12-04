from util import read_puzzle_input


def num_fully_contained_assignments(puzzle_input):
    num = 0
    for pair in puzzle_input.split("\n"):
        if pair == "":
            continue

        assignment_1, assignment_2 = pair.split(",")
        ass_1_start, ass_1_end = [int(num) for num in assignment_1.split("-")]
        ass_2_start, ass_2_end = [int(num) for num in assignment_2.split("-")]

        if ass_1_start <= ass_2_start and ass_1_end >= ass_2_end:
            num += 1
        elif ass_2_start <= ass_1_start and ass_2_end >= ass_1_end:
            num += 1
    return num


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_fully_contained_assignments(puzzle_input)}")
    print(f"Part 2: {num_fully_contained_assignments(puzzle_input)}")
