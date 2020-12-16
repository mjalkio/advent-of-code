from util import read_puzzle_input


def get_ticket_scanning_error_rate(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']

    rule_lines = lines[:lines.index('your ticket:')]
    # my_ticket_line = lines[lines.index('your ticket:') + 1]
    nearby_ticket_lines = lines[lines.index('nearby tickets:') + 1:]

    rules = {}
    for rule in rule_lines:
        field_name, range_definition = rule.split(': ')
        range_values = [r.split('-') for r in range_definition.split(' or ')]
        rules[field_name] = [range(int(rv[0]), int(rv[1]) + 1) for rv in range_values]

    all_valid_ranges = [valid_range for ranges in rules.values() for valid_range in ranges]

    ticket_scanning_error_rate = 0
    for ticket in nearby_ticket_lines:
        field_values = [int(field_value) for field_value in ticket.split(',')]
        for field_value in field_values:
            if not any(field_value in valid_range for valid_range in all_valid_ranges):
                ticket_scanning_error_rate += field_value
    return ticket_scanning_error_rate


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_ticket_scanning_error_rate(puzzle_input)}")
    print(f"Part 2: {None}")
