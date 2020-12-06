import inspect
from pathlib import Path


def read_puzzle_input(file_name='puzzle_input.txt'):
    caller_frame = inspect.stack()[1]
    caller_path = Path(caller_frame.filename)
    puzzle_input_path = Path(caller_path.parent, file_name)
    with puzzle_input_path.open() as f:
        puzzle_input_file_contents = f.read()

    # Sublime always adds a trailing newline, let's remove that
    puzzle_input = puzzle_input_file_contents[:-1]
    return puzzle_input
