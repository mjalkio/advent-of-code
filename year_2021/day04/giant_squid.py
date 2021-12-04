from util import read_puzzle_input

GRID_SIZE = 5


def get_winning_board_score(puzzle_input):
    inputs = puzzle_input.split('\n\n')
    numbers = [int(num) for num in inputs[0].split(',')]
    boards = [board.split() for board in inputs[1:]]

    board_possible_wins = []
    for b in boards:
        board_numbers = [int(num) for num in b]
        rows = []
        cols = []
        for i in range(GRID_SIZE):
            rows.append(board_numbers[i * GRID_SIZE:i * GRID_SIZE + GRID_SIZE])
            cols.append(board_numbers[i::GRID_SIZE])
        board_possible_wins.append({
            'rows': rows,
            'cols': cols,
        })

    for drawn_number in numbers:
        pass

    return 0


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_winning_board_score(puzzle_input)}")
    print(f"Part 2: {get_winning_board_score(puzzle_input)}")
