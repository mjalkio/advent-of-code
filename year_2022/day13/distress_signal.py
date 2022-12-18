from functools import cmp_to_key

from util import read_puzzle_input

DIVIDER_PACKETS = ["[[2]]", "[[6]]"]


def is_ordered(left, right):
    left_lst = eval(left)
    right_lst = eval(right)
    min_len = min(len(left_lst), len(right_lst))
    for i in range(min_len):
        if isinstance(left_lst[i], int) and isinstance(right_lst[i], int):
            if left_lst[i] < right_lst[i]:
                return True
            elif left_lst[i] > right_lst[i]:
                return False
            continue

        if isinstance(left_lst[i], int):
            left_lst[i] = [left_lst[i]]
        if isinstance(right_lst[i], int):
            right_lst[i] = [right_lst[i]]

        result = is_ordered(str(left_lst[i]), str(right_lst[i]))
        if result is not None:
            return result

    if len(left_lst) < len(right_lst):
        return True
    elif len(left_lst) > len(right_lst):
        return False

    return None


def sum_indices_ordered_pairs(puzzle_input):
    pairs = puzzle_input.split("\n\n")

    result = 0
    for i, pair in enumerate(pairs):
        left, right = pair.split("\n")
        if is_ordered(left, right):
            result += i + 1
    return result


def _comparator(left, right):
    if is_ordered(left, right):
        return -1
    return 1


def decoder_key(puzzle_input):
    packets = [
        line for line in puzzle_input.split("\n") if line != ""
    ] + DIVIDER_PACKETS
    sorted_packets = sorted(packets, key=cmp_to_key(_comparator))
    return (sorted_packets.index(DIVIDER_PACKETS[0]) + 1) * (
        sorted_packets.index(DIVIDER_PACKETS[1]) + 1
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_indices_ordered_pairs(puzzle_input)}")
    print(f"Part 2: {decoder_key(puzzle_input)}")
