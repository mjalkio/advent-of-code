from collections import namedtuple

from util import read_puzzle_input


Map = namedtuple("Map", ["dest_start", "source_start", "range_length"])


def get_lowest_location_number(puzzle_input):
    lines = puzzle_input.split("\n")
    seeds = [int(seed) for seed in lines.pop(0).split(": ")[1].split(" ")]
    while len(lines) > 0:
        lines = lines[2:]
        maps = []
        while len(lines) > 0 and lines[0] != "":
            maps.append(Map._make(int(num) for num in lines.pop(0).split(" ")))

        for i in range(len(seeds)):
            for m in maps:
                if m.source_start <= seeds[i] <= m.source_start + m.range_length - 1:
                    seeds[i] = m.dest_start + (seeds[i] - m.source_start)
                    break
    return min(seeds)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_lowest_location_number(puzzle_input)}")
    print(f"Part 2: {get_lowest_location_number(puzzle_input)}")
