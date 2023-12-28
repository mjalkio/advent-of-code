from util import read_puzzle_input


def sum_extrapolated_values(puzzle_input, backwards=False):
    histories = puzzle_input.split("\n")
    extrapolated_sum = 0
    for hist in histories:
        hist = [int(val) for val in hist.split(" ")]
        sequences = [hist]
        while any(num != 0 for num in sequences[-1]):
            values = sequences[-1]
            differences = [values[i + 1] - values[i] for i in range(len(values) - 1)]
            sequences.append(differences)

        sequences[-1].append(0)
        for i in reversed(range(len(sequences) - 1)):
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

        extrapolated_sum += sequences[0][-1]
    return extrapolated_sum


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_extrapolated_values(puzzle_input)}")
    print(f"Part 2: {sum_extrapolated_values(puzzle_input, backwards=True)}")
