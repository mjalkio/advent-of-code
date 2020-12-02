from collections import Counter


def is_valid_password(character, min_usages, max_usages, password):
    password_character_counts = Counter(password)
    if (
            password_character_counts[character] >= min_usages
            and password_character_counts[character] <= max_usages
    ):
        return True

    return False


def num_valid_passwords(puzzle_input):
    return None
