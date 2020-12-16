from util import read_puzzle_input


def _get_invalid_field_sum(ticket, all_valid_ranges):
    invalid_field_sum = 0
    for field_value in ticket:
        if not any(field_value in valid_range for valid_range in all_valid_ranges):
            invalid_field_sum += field_value
    return invalid_field_sum


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
        ticket_scanning_error_rate += _get_invalid_field_sum(ticket, all_valid_ranges)
    return ticket_scanning_error_rate


def get_field_order(puzzle_input):
    rules, my_ticket, nearby_tickets = _parse_input(puzzle_input)

    valid_tickets = [
        ticket
        for ticket
        in nearby_tickets
        if _get_invalid_field_sum(ticket, _get_all_valid_ranges(rules)) == 0
    ]
    valid_tickets.append(my_ticket)

    # Perform process of elimination. Start by saying any position could be any field.
    # Then go through the tickets and eliminate the fields that don't work.
    possible_fields = {position: list(rules.keys()) for position in range(len(my_ticket))}
    for position in range(len(my_ticket)):
        for ticket in valid_tickets:
            position_value = ticket[position]
            for field_name in list(possible_fields[position]):
                if not any(position_value in valid_range for valid_range in rules[field_name]):
                    possible_fields[position].remove(field_name)

    # In order for this problem to make sense, we must "know" some fields by now.
    # Keep eliminating the "known" fields from the other positions where they're included.
    while any(len(fields) > 1 for fields in possible_fields.values()):
        known_fields = [fields[0] for fields in possible_fields.values() if len(fields) == 1]
        for known_field_name in known_fields:
            for position in possible_fields:
                if (
                    len(possible_fields[position]) > 1
                    and known_field_name in possible_fields[position]
                ):
                    possible_fields[position].remove(known_field_name)

    return [possible_fields[position][0] for position in range(len(my_ticket))]


def get_departure_product(puzzle_input):
    _, my_ticket, _ = _parse_input(puzzle_input)
    field_order = get_field_order(puzzle_input)

    departure_product = 1
    for i, field_name in enumerate(field_order):
        if field_name.startswith('departure'):
            departure_product *= my_ticket[i]
    return departure_product


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_ticket_scanning_error_rate(puzzle_input)}")
    print(f"Part 2: {get_departure_product(puzzle_input)}")
