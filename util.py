import inspect
from pathlib import Path

import numpy as np

np.set_printoptions(linewidth=200)


def manhattan_distance(point_a, point_b):
    return sum(abs(a - b) for a, b in zip(point_a, point_b))


def read_puzzle_input(file_name="puzzle_input.txt"):
    caller_frame = inspect.stack()[1]
    caller_path = Path(caller_frame.filename)
    puzzle_input_path = Path(caller_path.parent, file_name)
    with puzzle_input_path.open() as f:
        puzzle_input_file_contents = f.read()

    # Sublime always adds a trailing newline, let's remove that
    if puzzle_input_file_contents[-1] == "\n":
        puzzle_input_file_contents = puzzle_input_file_contents[:-1]
    return puzzle_input_file_contents


def setup_day(year=""):
    problem_name = input("Enter the name of today's problem: ")
    problem_slug = problem_name.lower().replace(" ", "_")
    method_name = input("Enter the method name you plan to implement: ")
    test_result = input("Enter the part 1 test result: ")

    repo_dir = Path(__file__).parent
    year_dirs = [
        file
        for file in repo_dir.iterdir()
        if file.is_dir() and f"year_{year}" in file.name
    ]

    if len(year_dirs) == 0:
        new_year_dir = Path(repo_dir, f"year_{year}")
        new_year_dir.mkdir()
        Path(new_year_dir, "__init__.py").touch()

        year_dirs = [new_year_dir]

    year_dir = sorted(year_dirs)[-1]

    day_dirs = [
        file for file in year_dir.iterdir() if file.is_dir() and "day" in file.name
    ]

    if len(day_dirs) == 0:
        day_dirs = [Path(year_dir, "day00")]

    yesterday_dir = sorted(day_dirs)[-1]
    yesterday_day = yesterday_dir.name[3:]
    today_day = int(yesterday_day) + 1
    today_day_string = str(today_day).zfill(2)
    today_dir = Path(year_dir, f"day{today_day_string}")
    today_dir.mkdir()

    Path(today_dir, "__init__.py").touch()
    Path(today_dir, "puzzle_input.txt").touch()
    Path(today_dir, "test_input.txt").touch()

    problem_contents = f"""from util import read_puzzle_input


def {method_name}(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {{{method_name}(puzzle_input)}}")
    print(f"Part 2: {{{method_name}(puzzle_input)}}")
"""
    Path(today_dir, f"{problem_slug}.py").write_text(problem_contents)

    test_contents = f"""from util import read_puzzle_input
from {year_dir.name}.day{today_day_string}.{problem_slug} import (
    {method_name},
)


def test_{method_name}():
    assert {method_name}(read_puzzle_input("test_input.txt")) == {test_result}
"""
    Path(today_dir, f"test_{problem_slug}.py").write_text(test_contents)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Set up directory for a problem.")
    parser.add_argument("--year", default="")
    args = parser.parse_args()

    setup_day(year=args.year)
