from collections import defaultdict
from pathlib import Path

from util import read_puzzle_input


SMALL_DIRECTORY_SIZE = 100_000
TOTAL_DISK_SIZE = 70_000_000
UPDATE_SIZE = 30_000_000


def _get_directory_sizes(puzzle_input):
    lines = [line for line in puzzle_input.split("\n") if line != ""]
    assert lines[0] == "$ cd /"

    current_dir = Path("/")
    dir_sizes = defaultdict(int)

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
                    dir_sizes[current_dir] += int(file_size)

                    for parent_dir in current_dir.parents:
                        dir_sizes[parent_dir] += int(file_size)
                i += 1
        elif lines[i] == "$ cd ..":
            current_dir = current_dir.parent
            i += 1
        else:
            assert lines[i].startswith("$ cd ")
            current_dir = Path(current_dir, lines[i][5:])
            i += 1
    return dir_sizes


def sum_total_size_small_directories(puzzle_input):
    dir_sizes = _get_directory_sizes(puzzle_input)
    return sum(size for size in dir_sizes.values() if size <= SMALL_DIRECTORY_SIZE)


def get_directory_to_delete_size(puzzle_input):
    dir_sizes = _get_directory_sizes(puzzle_input)
    root_dir = Path("/")
    used_space = dir_sizes[root_dir]
    space_available = TOTAL_DISK_SIZE - used_space
    additional_space_needed = UPDATE_SIZE - space_available
    return min(size for size in dir_sizes.values() if size >= additional_space_needed)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_total_size_small_directories(puzzle_input)}")
    print(f"Part 2: {get_directory_to_delete_size(puzzle_input)}")
