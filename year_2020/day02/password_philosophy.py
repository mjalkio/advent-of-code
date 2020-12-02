from collections import Counter
from pathlib import Path


def is_valid_password_part_1(character, min_usages, max_usages, password):
    password_character_counts = Counter(password)
    if (
            password_character_counts[character] >= min_usages
            and password_character_counts[character] <= max_usages
    ):
        return True

    return False


def num_valid_passwords_part_1(puzzle_input):
    lines = [
        line
        for line
        in puzzle_input.split('\n')
        if line != ''
    ]

    num_valid = 0
    for line in lines:
        policy, password = line.split(':')
        character_range, character = policy.split(' ')
        min_usages, max_usages = [int(num) for num in character_range.split('-')]
        if is_valid_password_part_1(character, min_usages, max_usages, password):
            num_valid += 1
    return num_valid


def is_valid_password_part_2(character, position_1, position_2, password):
    is_char_at_position_1 = password[position_1 - 1] == character
    is_char_at_position_2 = password[position_2 - 1] == character
    return is_char_at_position_1 != is_char_at_position_2


def num_valid_passwords_part_2(puzzle_input):
    return None


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'part1_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_valid_passwords_part_1(puzzle_input)}")
