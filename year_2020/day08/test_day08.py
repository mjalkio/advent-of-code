from year_2020.day08.handheld_halting import (
    get_acc_at_infinite_loop_start,
    get_acc_at_program_termination,
)

TEST_INPUT = """
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""


def test_get_acc_at_infinite_loop_start():
    assert get_acc_at_infinite_loop_start(TEST_INPUT) == 5


def test_get_acc_at_termination_start():
    assert get_acc_at_program_termination(TEST_INPUT) == 8
