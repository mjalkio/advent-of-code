import math

from util import read_puzzle_input


def get_product_num_ways_beat_record(puzzle_input):
    time_input, distance_input = puzzle_input.split("\n")
    times = [int(t) for t in time_input.split("Time:")[1].split(" ") if t != ""]
    records = [
        int(d) for d in distance_input.split("Distance:")[1].split(" ") if d != ""
    ]
    races = zip(times, records)
    ways_to_beat_races = []
    for time, record in races:
        num_ways = 0
        for button_hold in range(1, time):
            distance = button_hold * (time - button_hold)
            if distance > record:
                num_ways += 1
        ways_to_beat_races.append(num_ways)
    return math.prod(ways_to_beat_races)


def get_num_ways_to_beat_record(puzzle_input):
    time_input, distance_input = puzzle_input.split("\n")
    time = int(time_input.split("Time:")[1].replace(" ", ""))
    record = int(distance_input.split("Distance:")[1].replace(" ", ""))
    num_ways = 0
    for button_hold in range(1, time):
        distance = button_hold * (time - button_hold)
        if distance > record:
            num_ways += 1
    return num_ways


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_product_num_ways_beat_record(puzzle_input)}")
    print(f"Part 2: {get_num_ways_to_beat_record(puzzle_input)}")
