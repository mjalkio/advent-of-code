import math
from functools import reduce

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


def _chinese_remainder(n, a):
    """Source: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python"""
    total_sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        total_sum += a_i * _mul_inv(p, n_i) * p
    return total_sum % prod


def _mul_inv(a, b):
    """Source: https://rosettacode.org/wiki/Chinese_remainder_theorem#Python"""
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def get_bus_id_times_wait_time(puzzle_input):
    return math.prod(get_earliest_bus_and_wait_time_for_airport(puzzle_input))


def get_shuttle_company_solution(puzzle_input):
    """This is a Chinese remainder theorem problem.
    If we take the first example input: 7,13,x,x,59,x,31,19
    We can translate this to the following series of equations:
        t % 7 = 0           =>      t = 0 (mod 7)
        (t + 1) % 13 = 0    =>      t = 12 (mod 13)
        (t + 4) % 59 = 0    =>      t = 55 (mod 59)
        (t + 6) % 31 = 0    =>      t = 25 (mod 31)
        (t + 7) % 19 = 0    =>      t = 12 (mod 19)

    Solving this requires math, which I took from Rosetta Code. Math is hard.
    """
    _, bus_notes = [line for line in puzzle_input.split('\n') if line != '']
    mod_values = []
    congruent_values = []
    for i, bus_id in enumerate(bus_notes.split(',')):
        if bus_id == 'x':
            continue
        n = int(bus_id)
        mod_values.append(n)
        congruent_values.append(n - i)
    return _chinese_remainder(n=mod_values, a=congruent_values)


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_bus_id_times_wait_time(puzzle_input)}")
    print(f"Part 2: {get_shuttle_company_solution(puzzle_input)}")
