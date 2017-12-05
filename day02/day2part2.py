def _calculate_line_checksum(line):
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i] % line[j] == 0:
                return line[i] / line[j]
            elif line[j] % line[i] == 0:
                return line[j] / line[i]
    raise Exception("This shouldn't happen!")


def calculate_checksum_divisible(puzzle_input):
    checksum = 0
    puzzle_input = puzzle_input.split('\n')
    for line in puzzle_input:
        line = line.split()
        if len(line) == 0:
            continue
        line = [element for element in line if len(element) > 0]
        line = [int(num) for num in line]
        checksum += _calculate_line_checksum(line)

    return checksum
