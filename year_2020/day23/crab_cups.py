def get_crab_cups(puzzle_input, num_moves=100):
    cups = [int(label) for label in puzzle_input]
    highest_label = max(cups)
    lowest_label = min(cups)
    for _ in range(num_moves):
        current_cup_label = cups[0]
        destination_cup_label = current_cup_label - 1
        while destination_cup_label not in cups[4:]:
            destination_cup_label -= 1

            if destination_cup_label < lowest_label:
                destination_cup_label = highest_label

        destination_cup_idx = cups.index(destination_cup_label)
        cups = (
            # cups[4] is the new current cup because it will be clockwise of the old current cup
            cups[4:destination_cup_idx + 1]
            # Place cups clockwise of the destination cup
            + cups[1:4]
            # This part of the list doesn't change
            + cups[destination_cup_idx + 1:]
            # The old current cup is counter clockwise of the new current cup
            + cups[0:1]
        )

    one_idx = cups.index(1)
    return ''.join(str(label) for label in cups[one_idx + 1:] + cups[:one_idx])


if __name__ == '__main__':
    puzzle_input = '792845136'

    print(f"Part 1: {get_crab_cups(puzzle_input)}")
    print(f"Part 2: {None}")
