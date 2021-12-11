def get_crab_cups(puzzle_input, num_moves=100, is_part_two=False):
    cups = [int(label) for label in puzzle_input]

    cup_circle = {}
    for i in range(1, len(cups) + 1):
        cup_circle[i] = cups[(cups.index(i) + 1) % len(cups)]

    if is_part_two:
        cup_circle[cups[-1]] = 10
        for i in range(10, 1_000_000):
            cup_circle[i] = i + 1
        cup_circle[1_000_000] = cups[0]

    highest_label = max(cup_circle)
    lowest_label = min(cup_circle)
    current_cup_label = cups[0]
    for _ in range(num_moves):
        cup_labels_to_move = (
            cup_circle[current_cup_label],
            cup_circle[cup_circle[current_cup_label]],
            cup_circle[cup_circle[cup_circle[current_cup_label]]],
        )

        destination_cup_label = current_cup_label - 1
        while (
            destination_cup_label in cup_labels_to_move
            or destination_cup_label < lowest_label
        ):
            destination_cup_label -= 1

            if destination_cup_label < lowest_label:
                destination_cup_label = highest_label

        cup_circle[current_cup_label] = cup_circle[cup_labels_to_move[-1]]
        cup_circle[cup_labels_to_move[-1]] = cup_circle[destination_cup_label]
        cup_circle[destination_cup_label] = cup_labels_to_move[0]

        current_cup_label = cup_circle[current_cup_label]

    if is_part_two:
        return cup_circle[1] * cup_circle[cup_circle[1]]

    cups_after_1 = ""
    next_cup = cup_circle[1]
    while next_cup != 1:
        cups_after_1 += str(next_cup)
        next_cup = cup_circle[next_cup]
    return cups_after_1


if __name__ == "__main__":
    puzzle_input = "792845136"

    print(f"Part 1: {get_crab_cups(puzzle_input)}")
    print(
        f"Part 2: {get_crab_cups(puzzle_input, num_moves=10000000, is_part_two=True)}"
    )
