from day8part1 import get_input, get_largest_register_value


EXAMPLE_FILE_NAME = 'example.txt'


def test_get_largest_register_value():
    instructions = get_input(EXAMPLE_FILE_NAME)
    assert get_largest_register_value(instructions) == 1
