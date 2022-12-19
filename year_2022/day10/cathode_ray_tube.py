from util import read_puzzle_input


def _render_image(image, pos, X):
    if pos % 40 == 0:
        image += "\n"

    if pos % 40 in range(X - 1, X + 2):
        image += "#"
    else:
        image += "."
    return image


def sum_interesting_signal_strengths(puzzle_input):
    instructions = [line for line in puzzle_input.split("\n") if line != ""]
    cycle_value = 1
    X = 1
    signal_strengths = []
    image = ""
    for instr in instructions:
        image = _render_image(image=image, pos=cycle_value - 1, X=X)
        signal_strengths.append(cycle_value * X)
        if instr == "noop":
            cycle_value += 1
        else:
            V = int(instr[5:])
            cycle_value += 1
            image = _render_image(image=image, pos=cycle_value - 1, X=X)
            signal_strengths.append(cycle_value * X)
            X += V
            cycle_value += 1
    return sum(
        signal_strengths[i] for i in range(len(signal_strengths)) if (i - 19) % 40 == 0
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_interesting_signal_strengths(puzzle_input)}")
