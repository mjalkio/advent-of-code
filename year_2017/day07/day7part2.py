from collections import Counter

from day7part1 import get_input


def parse_program_name(line):
    return line.split("(")[0].strip()


def parse_program_weight(line):
    return int(line.split("(")[1].split(")")[0])


def parse_program_children(line):
    if "->" not in line:
        return None
    return line.split("->")[1].strip().split(", ")


def get_program_weights(lines):
    return {parse_program_name(line): parse_program_weight(line) for line in lines}


def get_program_children(lines):
    return {
        parse_program_name(line): parse_program_children(line)
        for line in lines
        if parse_program_children(line) is not None
    }


def has_no_unbalanced_children(program, program_children, weights):
    if program not in program_children:
        # Has no children, so they can't be unbalanced
        return True

    children = program_children[program]
    child_weights = [weights[child] for child in children]
    if len(set(child_weights)) != 1:
        return False

    return all(
        [
            has_no_unbalanced_children(child, program_children, weights)
            for child in children
        ]
    )


def wrong_weight_disc_correction(puzzle_input):
    lines = puzzle_input.strip().split("\n")
    program_weights = get_program_weights(lines)
    program_children = get_program_children(lines)
    program_balanced_weights = {}

    # Correct thing to do here is probably topological sort, but I'm lazy
    while len(program_weights) != len(program_balanced_weights):
        for program in program_weights:
            if program in program_balanced_weights:
                # Already calculated weight, skip
                continue
            elif program not in program_children:
                # This is a leaf node, we have its weight
                program_balanced_weights[program] = program_weights[program]
            elif all(
                [
                    child in program_balanced_weights
                    for child in program_children[program]
                ]
            ):
                # We've calculated the weights for all children
                weight = program_weights[program]
                weight += sum(
                    [
                        program_balanced_weights[child]
                        for child in program_children[program]
                    ]
                )
                program_balanced_weights[program] = weight
            else:
                # Need to do more rounds before can do weight for this program
                continue

    # Now we need to figure out which disc is the oddball
    for _, children in program_children.items():
        child_weights = {child: program_balanced_weights[child] for child in children}
        if len(set(child_weights.values())) == 1:
            # All the same weight, we're good!
            continue

        msg = "Need 3+ children to decide correct weight."
        assert len(child_weights) > 2, msg

        counts = Counter(child_weights.values())

        msg = "Should only have one correct weight and one incorrect weight"
        assert len(counts) == 2, msg

        good_weight, bad_weight = [w for (w, cnt) in counts.most_common()]
        adjustment = good_weight - bad_weight
        for child, weight in child_weights.items():
            if weight == bad_weight and has_no_unbalanced_children(
                child,
                program_children,
                program_balanced_weights,
            ):
                # Needs to be the root of the problem to return
                return program_weights[child] + adjustment

    raise ValueError("Michael messed up this problem.")


if __name__ == "__main__":
    puzzle_input = get_input("puzzle_input.txt")
    print(wrong_weight_disc_correction(puzzle_input))
