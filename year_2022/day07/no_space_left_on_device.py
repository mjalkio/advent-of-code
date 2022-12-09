from collections import defaultdict
from pathlib import Path

from util import read_puzzle_input


SMALL_DIRECTORY_SIZE = 100_000


def sum_total_size_small_directories(puzzle_input):
    lines = [line for line in puzzle_input.split("\n") if line != ""]
    assert lines[0] == "$ cd /"

    current_dir = Path("/")
    total_sizes = defaultdict(int)

    i = 1
    while i < len(lines):
        if lines[i] == "$ ls":
            # Note: I am assuming we don't `ls` the same directory twice
            i += 1
            while i < len(lines) and not lines[i].startswith("$"):
                if lines[i].startswith("dir "):
                    pass
                else:
                    file_size, file_name = lines[i].split()
                    total_sizes[current_dir] += int(file_size)

                    for parent_dir in current_dir.parents:
                        total_sizes[parent_dir] += int(file_size)
                i += 1
        elif lines[i] == "$ cd ..":
            current_dir = current_dir.parent
            i += 1
        else:
            assert lines[i].startswith("$ cd ")
            current_dir = Path(current_dir, lines[i][5:])
            i += 1
    return sum(size for size in total_sizes.values() if size <= SMALL_DIRECTORY_SIZE)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_total_size_small_directories(puzzle_input)}")
    print(f"Part 2: {sum_total_size_small_directories(puzzle_input)}")
