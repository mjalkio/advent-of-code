def calculate_checksum(puzzle_input):
    checksum = 0
    puzzle_input = puzzle_input.split('\n')
    for line in puzzle_input:
        line = line.split()
        if len(line) == 0:
            continue
        line = [element for element in line if len(element) > 0]
        line = [int(num) for num in line]
        checksum += max(line) - min(line)

    return checksum
