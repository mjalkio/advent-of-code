from util import read_puzzle_input


def _get_ticket_scanning_error_rate(ticket, all_valid_ranges):
    ticket_scanning_error_rate = 0
    for field_value in ticket:
        if not any(field_value in valid_range for valid_range in all_valid_ranges):
            ticket_scanning_error_rate += field_value
    return ticket_scanning_error_rate


def _parse_input(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']

    rule_lines = lines[:lines.index('your ticket:')]
    my_ticket_line = lines[lines.index('your ticket:') + 1]
    nearby_ticket_lines = lines[lines.index('nearby tickets:') + 1:]

    rules = {}
    for rule in rule_lines:
        field_name, range_definition = rule.split(': ')
        range_values = [r.split('-') for r in range_definition.split(' or ')]
        rules[field_name] = [range(int(rv[0]), int(rv[1]) + 1) for rv in range_values]

    my_ticket = [int(field_value) for field_value in my_ticket_line.split(',')]
    nearby_tickets = [
        [int(field_value) for field_value in ticket_line.split(',')]
        for ticket_line
        in nearby_ticket_lines
    ]

    return rules, my_ticket, nearby_tickets


def _get_all_valid_ranges(rules):
    return [valid_range for ranges in rules.values() for valid_range in ranges]


def get_ticket_scanning_error_rate(puzzle_input):
    rules, _, nearby_tickets = _parse_input(puzzle_input)

    all_valid_ranges = _get_all_valid_ranges(rules)

    ticket_scanning_error_rate = 0
    for ticket in nearby_tickets:
        ticket_scanning_error_rate += _get_ticket_scanning_error_rate(ticket, all_valid_ranges)
    return ticket_scanning_error_rate


def get_field_order(puzzle_input):
    return None


def get_departure_sum(puzzle_input):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_ticket_scanning_error_rate(puzzle_input)}")
    print(f"Part 2: {get_departure_sum(puzzle_input)}")
