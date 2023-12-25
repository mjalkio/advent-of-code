from collections import namedtuple

from util import read_puzzle_input


Map = namedtuple("Map", ["source_range", "dest_start"])
Range = namedtuple("Range", ["start", "end"])


def get_lowest_location_number(puzzle_input, use_ranges=False):
    lines = puzzle_input.split("\n")
    seeds = [int(seed) for seed in lines.pop(0).split(": ")[1].split(" ")]
    seed_ranges = []
    if use_ranges:
        while len(seeds) > 0:
            start = seeds.pop(0)
            num_values = seeds.pop(0)
            seed_ranges.append(Range(start=start, end=start + num_values - 1))
    else:
        seed_ranges = [Range(start=seed, end=seed) for seed in seeds]
    seed_ranges.sort()

    while len(lines) > 0:
        lines = lines[2:]
        maps = []
        while len(lines) > 0 and lines[0] != "":
            dest_start, source_start, range_length = [
                int(num) for num in lines.pop(0).split(" ")
            ]
            maps.append(
                Map(
                    source_range=Range(
                        start=source_start, end=source_start + range_length - 1
                    ),
                    dest_start=dest_start,
                )
            )
        maps.sort()

        seed_idx = 0
        map_idx = 0
        new_seed_ranges = []
        while seed_idx < len(seed_ranges) and map_idx < len(maps):
            s_range = seed_ranges[seed_idx]
            m_range = maps[map_idx]
            if s_range.end < m_range.source_range.start:
                # Entire seed range is before map range
                new_seed_ranges.append(s_range)
                seed_idx += 1
                continue

            if s_range.start > m_range.source_range.end:
                # Entire seed range is after map range
                map_idx += 1
                continue

            if s_range.start < m_range.source_range.start:
                # Has some part of it before the map
                new_seed_ranges.append(
                    Range(start=s_range.start, end=m_range.source_range.start)
                )
                s_range = Range(start=m_range.source_range.start, end=s_range.end)

            # Handle the overlap
            if s_range.end <= m_range.source_range.end:
                # Rest of the seed range is within the map range
                new_seed_ranges.append(
                    Range(
                        start=m_range.dest_start
                        + (s_range.start - m_range.source_range.start),
                        end=m_range.dest_start
                        + (s_range.end - m_range.source_range.start),
                    )
                )
                seed_idx += 1
                continue
            # Now we know that the seed is bigger than the map
            new_seed_ranges.append(
                Range(
                    start=m_range.dest_start
                    + (s_range.start - m_range.source_range.start),
                    end=m_range.dest_start
                    + (m_range.source_range.end - m_range.source_range.start),
                )
            )
            seed_ranges[seed_idx] = Range(
                start=m_range.source_range.end, end=s_range.end
            )
            map_idx += 1
        new_seed_ranges.sort()
        seed_ranges = new_seed_ranges
    return min(s_range.start for s_range in seed_ranges)


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_lowest_location_number(puzzle_input)}")
    print(f"Part 2: {get_lowest_location_number(puzzle_input, use_ranges=True)}")
