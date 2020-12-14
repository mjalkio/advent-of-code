import math

from util import read_puzzle_input


def get_earliest_bus_and_wait_time_for_airport(puzzle_input):
    earliest_departure_note, bus_notes = [line for line in puzzle_input.split('\n') if line != '']
    earliest_departure = int(earliest_departure_note)
    buses = [int(bus_id) for bus_id in bus_notes.split(',') if bus_id != 'x']
    possible_departure = earliest_departure
    while True:
        for bus_id in buses:
            if possible_departure % bus_id == 0:
                return bus_id, possible_departure - earliest_departure
        possible_departure += 1


def get_bus_id_times_wait_time(puzzle_input):
    return math.prod(get_earliest_bus_and_wait_time_for_airport(puzzle_input))


def get_shuttle_company_solution(puzzle_input):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_bus_id_times_wait_time(puzzle_input)}")
    print(f"Part 2: {get_shuttle_company_solution(puzzle_input)}")
