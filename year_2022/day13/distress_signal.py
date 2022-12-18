from util import read_puzzle_input


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
    elif len(right_lst) > len(left_lst):
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


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_indices_ordered_pairs(puzzle_input)}")
    print(f"Part 2: {sum_indices_ordered_pairs(puzzle_input)}")
