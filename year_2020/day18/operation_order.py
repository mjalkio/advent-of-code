import operator

from util import read_puzzle_input

OPERATORS = {
    '+': operator.add,
    '*': operator.mul,
}


def _parse_out_parentheses(expression):
    num_open_parens = 0
    for i in range(len(expression)):
        if expression[i] == '(':
            num_open_parens += 1
        elif expression[i] == ')':
            num_open_parens -= 1

        if num_open_parens == 0:
            return expression[:i + 1].strip(), expression[i + 1:].strip()


def _parse_out_number(expression):
    for i in range(len(expression)):
        if expression[i] in OPERATORS or expression[i] == '(':
            return expression[:i].strip(), expression[i:].strip()
    return expression, ''


def _parse_out_operator(expression):
    for i in range(len(expression)):
        if expression[i] in OPERATORS:
            return OPERATORS[expression[i]], expression[i + 1:].strip()


def _split_expression(expression):
    """Split expression and return left_part, operator, right_part, remainder"""
    if expression.startswith('('):
        left_part, left_remainder = _parse_out_parentheses(expression)
    else:
        left_part, left_remainder = _parse_out_number(expression)

    if left_remainder == '':
        return left_part, None, None, None

    operator, operator_remainder = _parse_out_operator(left_remainder)

    if operator_remainder.startswith('('):
        right_part, remainder = _parse_out_parentheses(operator_remainder)
    else:
        right_part, remainder = _parse_out_number(operator_remainder)

    return left_part, operator, right_part, remainder


def evaluate_expression(expression, advanced_math=False):
    if advanced_math:
        expression = transform_to_advanced_math(expression)

    left_part, operator, right_part, remainder = _split_expression(expression)

    if left_part.startswith('('):
        evaluated_left_part = evaluate_expression(left_part[1:-1])
    else:
        evaluated_left_part = int(left_part)

    if operator is None:
        return evaluated_left_part

    if right_part.startswith('('):
        evaluated_right_part = evaluate_expression(right_part[1:-1])
    else:
        evaluated_right_part = int(right_part)

    operation_result = operator(evaluated_left_part, evaluated_right_part)
    return evaluate_expression(f"{operation_result}{remainder}")


def transform_to_advanced_math(expression):
    return None


def sum_of_expressions(puzzle_input):
    return sum(
        evaluate_expression(expression)
        for expression
        in puzzle_input.split('\n')
        if expression != ''
    )


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {sum_of_expressions(puzzle_input)}")
    print(f"Part 2: {None}")
