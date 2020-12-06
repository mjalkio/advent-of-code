from collections import Counter

from util import read_puzzle_input


def num_questions_answered_by_group(group_input):
    questions_only = group_input.replace(' ', '').replace('\n', '')
    question_counts = Counter(questions_only)
    return len(question_counts)


def sum_questions_answered_by_group(puzzle_input):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_questions_answered_by_group(puzzle_input)}")
    print(f"Part 2: {None}")
