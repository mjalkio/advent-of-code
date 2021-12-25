w = "w"
x = "x"
y = "y"
z = "z"


def run_program(program, inputs):
    state = {
        w: 0,
        x: 0,
        y: 0,
        z: 0,
    }
    input_idx = 0
    for line in program.split("\n"):
        instruction = line[:3]
        if instruction == "inp":
            variable = line[4]
            state[variable] = inputs[input_idx]
            input_idx += 1
            continue

        a, b = line[4:].split(" ")

        if b in state:
            b = state[b]
        else:
            b = int(b)

        if instruction == "add":
            result = state[a] + b
        elif instruction == "mul":
            result = state[a] * b
        elif instruction == "div":
            result = state[a] // b
        elif instruction == "mod":
            result = state[a] % b
        elif instruction == "eql":
            result = int(state[a] == b)
        else:
            raise ValueError("Unexpected instruction")
        state[a] = result
    return state


if __name__ == "__main__":
    # Solved manually, see notepad_3.txt
    print("Part 1: 91599994399395")
    print("Part 2: 71111591176151")
