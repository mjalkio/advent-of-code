from util import read_puzzle_input


def sum_of_common_priorities(puzzle_input):
    answer = 0
    for line in puzzle_input.split("\n"):
        if line == "":
            continue

        assert len(line) % 2 == 0
        first = line[: len(line) // 2]
        second = line[len(line) // 2 :]
        common = set(first).intersection(set(second))
        assert len(common) == 1
        common_item = common.pop()

        if common_item >= "a":
            # Lowercase letter
            answer += ord(common_item) - ord("a") + 1
        else:
            # Uppercase letter
            answer += ord(common_item) - ord("A") + 1 + 26
    return answer


def sum_of_badge_priorities(puzzle_input):
    answer = 0
    rucksacks = [line for line in puzzle_input.split("\n") if line != ""]
    while len(rucksacks) > 0:
        first = rucksacks.pop(0)
        second = rucksacks.pop(0)
        third = rucksacks.pop(0)

        common = set(first).intersection(set(second)).intersection(set(third))
        assert len(common) == 1
        common_item = common.pop()

        if common_item >= "a":
            # Lowercase letter
            answer += ord(common_item) - ord("a") + 1
        else:
            # Uppercase letter
            answer += ord(common_item) - ord("A") + 1 + 26
    return answer


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_of_common_priorities(puzzle_input)}")
    print(f"Part 2: {sum_of_badge_priorities(puzzle_input)}")
