from util import read_puzzle_input


def _is_symbol(char):
    return char != "." and not char.isdigit()


def _is_part_number(lines, line_num, start, end):
    min_x = max(0, start - 1)
    max_x = min(len(lines[0]), end + 1)

    if line_num > 0:
        # Check above
        for x in range(min_x, max_x):
            if _is_symbol(lines[line_num - 1][x]):
                return True
    if len(lines) > line_num + 1:
        # Check below
        for x in range(min_x, max_x):
            if _is_symbol(lines[line_num + 1][x]):
                return True

    if _is_symbol(lines[line_num][min_x]) or _is_symbol(lines[line_num][max_x - 1]):
        return True

    return False


def sum_part_numbers(puzzle_input):
    lines = puzzle_input.split("\n")
    potential_parts = []
    for line_num, line in enumerate(lines):
        i = 0
        while i < len(line):
            if line[i].isdigit():
                num = ""
                start = i
                while i < len(line) and line[i].isdigit():
                    num += line[i]
                    i += 1
                end = i
                potential_parts.append((num, line_num, start, end))
            else:
                i += 1

    answer = 0
    for num, line_num, start, end in potential_parts:
        if _is_part_number(lines, line_num, start, end):
            answer += int(num)
    return answer


def sum_gear_ratios(puzzle_input):
    return 0


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_part_numbers(puzzle_input)}")
    print(f"Part 2: {sum_gear_ratios(puzzle_input)}")
