from day8 import execute_instructions, get_input


EXAMPLE_FILE_NAME = 'example.txt'


def test_execute_instructions():
    instructions = get_input(EXAMPLE_FILE_NAME)
    max_val, max_ever = execute_instructions(instructions)
    assert max_val == 1
    assert max_ever == 10
