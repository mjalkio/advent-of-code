import inspect
from pathlib import Path

import numpy as np

np.set_printoptions(linewidth=200)


def read_puzzle_input(file_name='puzzle_input.txt'):
    caller_frame = inspect.stack()[1]
    caller_path = Path(caller_frame.filename)
    puzzle_input_path = Path(caller_path.parent, file_name)
    with puzzle_input_path.open() as f:
        puzzle_input_file_contents = f.read()

    # Sublime always adds a trailing newline, let's remove that
    puzzle_input = puzzle_input_file_contents[:-1]
    return puzzle_input


def setup_day():
    repo_dir = Path(__file__).parent
    year_dirs = [
        file
        for file in repo_dir.iterdir()
        if file.is_dir() and 'year' in file.name
    ]
    current_year_dir = sorted(year_dirs)[-1]
    print(current_year_dir)


if __name__ == '__main__':
    setup_day()
