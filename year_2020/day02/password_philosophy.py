from collections import Counter
from pathlib import Path


def _parse_puzzle_input(puzzle_input):
    lines = [
        line
        for line
        in puzzle_input.split('\n')
        if line != ''
    ]

    parsed_input = []
    for line in lines:
        policy, password = [s.strip() for s in line.split(':')]
        character_range, character = policy.split(' ')
        num_1, num_2 = [int(num) for num in character_range.split('-')]
        parsed_input.append({
            'character': character,
            'num_1': num_1,
            'num_2': num_2,
            'password': password,
        })
    return parsed_input


def is_valid_password_part_1(character, min_usages, max_usages, password):
    password_character_counts = Counter(password)
    if (
            password_character_counts[character] >= min_usages
            and password_character_counts[character] <= max_usages
    ):
        return True

    return False


def num_valid_passwords_part_1(puzzle_input):
    parsed_input = _parse_puzzle_input(puzzle_input)

    num_valid = 0
    for password_data in parsed_input:
        if is_valid_password_part_1(
            character=password_data['character'],
            min_usages=password_data['num_1'],
            max_usages=password_data['num_2'],
            password=password_data['password'],
        ):
            num_valid += 1
    return num_valid


def is_valid_password_part_2(character, position_1, position_2, password):
    is_char_at_position_1 = password[position_1 - 1] == character
    is_char_at_position_2 = password[position_2 - 1] == character
    return is_char_at_position_1 != is_char_at_position_2


def num_valid_passwords_part_2(puzzle_input):
    parsed_input = _parse_puzzle_input(puzzle_input)

    num_valid = 0
    for password_data in parsed_input:
        if is_valid_password_part_2(
            character=password_data['character'],
            position_1=password_data['num_1'],
            position_2=password_data['num_2'],
            password=password_data['password'],
        ):
            num_valid += 1
    return num_valid


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'part1_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_valid_passwords_part_1(puzzle_input)}")
    print(f"Part 2: {num_valid_passwords_part_2(puzzle_input)}")
