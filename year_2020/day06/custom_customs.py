from collections import Counter

from util import read_puzzle_input


def num_questions_answered_by_group(group_input):
    questions_only = group_input.replace(" ", "").replace("\n", "")
    question_counts = Counter(questions_only)
    return len(question_counts)


def sum_questions_answered_by_group(puzzle_input):
    group_inputs = puzzle_input.split("\n\n")
    return sum(num_questions_answered_by_group(gi) for gi in group_inputs)


def num_questions_answered_by_whole_group(group_input):
    individual_questions_answered = [
        set(questions) for questions in group_input.split("\n") if questions != ""
    ]
    return len(set.intersection(*individual_questions_answered))


def sum_questions_answered_by_whole_group(puzzle_input):
    group_inputs = puzzle_input.split("\n\n")
    return sum(num_questions_answered_by_whole_group(gi) for gi in group_inputs)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_questions_answered_by_group(puzzle_input)}")
    print(f"Part 2: {sum_questions_answered_by_whole_group(puzzle_input)}")
