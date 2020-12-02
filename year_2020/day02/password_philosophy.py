from collections import Counter
from pathlib import Path


def is_valid_password(character, min_usages, max_usages, password):
    password_character_counts = Counter(password)
    if (
            password_character_counts[character] >= min_usages
            and password_character_counts[character] <= max_usages
    ):
        return True

    return False


def num_valid_passwords(puzzle_input):
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
        if is_valid_password(character, min_usages, max_usages, password):
            num_valid += 1
    return num_valid


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'part1_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    print(f"Part 1: {num_valid_passwords(puzzle_input)}")
