from collections import namedtuple

from util import read_puzzle_input

GRID_SIZE = 5

Board = namedtuple("Board", ["rows", "cols", "all_nums"])


def _get_boards(board_inputs):
    board_strings = [board.split() for board in board_inputs]
    boards = []
    for b in board_strings:
        board_numbers = [int(num) for num in b]
        rows = []
        cols = []
        for i in range(GRID_SIZE):
            rows.append(board_numbers[i * GRID_SIZE : i * GRID_SIZE + GRID_SIZE])
            cols.append(board_numbers[i::GRID_SIZE])
        boards.append(Board(rows=rows, cols=cols, all_nums=board_numbers))
    return boards


def _has_win(sequences, drawn_numbers):
    return any([len(set(seq) - drawn_numbers) == 0 for seq in sequences])


def get_winning_board_score(puzzle_input):
    inputs = puzzle_input.split("\n\n")
    numbers = [int(num) for num in inputs[0].split(",")]
    boards = _get_boards(inputs[1:])

    for move_num in range(len(numbers)):
        drawn_numbers = set(numbers[: move_num + 1])
        for b in boards:
            if _has_win(b.rows, drawn_numbers) or _has_win(b.cols, drawn_numbers):
                return sum(set(b.all_nums) - drawn_numbers) * numbers[move_num]


def get_losing_board_score(puzzle_input):
    inputs = puzzle_input.split("\n\n")
    numbers = [int(num) for num in inputs[0].split(",")]
    non_winning_boards = _get_boards(inputs[1:])

    for move_num in range(len(numbers)):
        drawn_numbers = set(numbers[: move_num + 1])

        winners = []
        for b in non_winning_boards:
            if _has_win(b.rows, drawn_numbers) or _has_win(b.cols, drawn_numbers):
                if len(non_winning_boards) == 1:
                    return sum(set(b.all_nums) - drawn_numbers) * numbers[move_num]

                winners.append(b)
        for w in winners:
            non_winning_boards.remove(w)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_winning_board_score(puzzle_input)}")
    print(f"Part 2: {get_losing_board_score(puzzle_input)}")
