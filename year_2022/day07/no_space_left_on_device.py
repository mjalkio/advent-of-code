from collections import defaultdict

from util import read_puzzle_input


def sum_total_size_small_directories(puzzle_input):
    lines = [line for line in puzzle_input.split("\n") if line != ""]
    assert lines[0] == "$ cd /"

    current_dir = "/"
    all_dirs = set("/")
    parent_dirs = {}
    direct_files_size = defaultdict(int)
    subdirs = defaultdict(list)

    i = 1
    while i < len(lines):
        if lines[i] == "$ ls":
            i += 1
            while i < len(lines) and not lines[i].startswith("$"):
                if lines[i].startswith("dir "):
                    subdir = lines[i][4:]
                    all_dirs.add(subdir)
                    subdirs[current_dir].append(subdir)
                    parent_dirs[subdir] = current_dir
                else:
                    file_size, file_name = lines[i].split()
                    direct_files_size[current_dir] += int(file_size)
                i += 1
        elif lines[i] == "$ cd ..":
            current_dir = parent_dirs[current_dir]
            i += 1
        else:
            assert lines[i].startswith("$ cd ")
            current_dir = lines[i][5:]
            i += 1
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_total_size_small_directories(puzzle_input)}")
    print(f"Part 2: {sum_total_size_small_directories(puzzle_input)}")
