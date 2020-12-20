import itertools
from collections import defaultdict

from util import read_puzzle_input


def _parse_rules(rule_definitions):
    lines = [line for line in rule_definitions.split('\n') if line != '']
    rules = defaultdict(list)
    for line in lines:
        rule_num_definition, definition = line.split(': ')
        rule_num = int(rule_num_definition)

        subrule_definitions = definition.split(' | ')
        for subrule_def in subrule_definitions:
            subrules = subrule_def.split(' ')
            rules[int(rule_num)].append(
                [
                    int(subrule) if subrule.isdigit() else subrule
                    for subrule
                    in subrules
                ]
            )
    return rules


def get_valid_messages(rule_definitions, max_valid_message_length=100):
    rules_to_valid_messages = {}
    rules = _parse_rules(rule_definitions)
    while len(rules_to_valid_messages) < len(rules):
        num_rules_handled = len(rules_to_valid_messages)
        for rule_num, subrule_lists in rules.items():
            if rule_num in rules_to_valid_messages.keys():
                # We've already included the valid messages for this rule
                continue

            if not type(subrule_lists[0][0]) == int:
                # If it's not a digit, it's a single character rule
                # Single character rules can be added immediately
                single_character_rule = subrule_lists[0][0]
                rules_to_valid_messages[rule_num] = {single_character_rule[1:-1]}
                continue

            # This rule depends on other rules
            all_required_subrules = [rule for subrule in subrule_lists for rule in subrule]
            if not all(rule in rules_to_valid_messages.keys() for rule in all_required_subrules):
                # We can't define this rule yet
                continue
            valid_messages_for_rule = set()
            for subrule_list in subrule_lists:
                valid_messages_for_list = None
                while len(subrule_list) > 0:
                    subrule = subrule_list.pop(0)
                    valid_messages_for_subrule = rules_to_valid_messages[subrule]
                    if valid_messages_for_list is None:
                        valid_messages_for_list = valid_messages_for_subrule
                    else:
                        valid_messages_for_list = set([
                            ''.join(message_parts)
                            for message_parts
                            in itertools.product(
                                valid_messages_for_list,
                                valid_messages_for_subrule
                            )
                        ])
                valid_messages_for_rule = valid_messages_for_rule.union(valid_messages_for_list)
            rules_to_valid_messages[rule_num] = valid_messages_for_rule

        if num_rules_handled == len(rules_to_valid_messages):
            # No new rules were defined in this iteration.
            # This means we have infinite loops.
            # We should generate valid messages up to the max length of the valid messages in our input.
            # We happen to know that only rules 8 and 11 contain infinite loops.
            rule_8 = rules[8]
            rule_11 = rules[11]
            break
    return rules_to_valid_messages


def does_message_match_rules(rules, rule_num, message, valid_messages=None):
    if valid_messages is None:
        # It takes time to get valid messages, allow us to calculate once
        valid_messages = get_valid_messages(rules)
    return message in valid_messages[rule_num]


def num_messages_match_rule(puzzle_input, add_infinite_loops=False, rule_num=0):
    rule_definitions, messages = puzzle_input.split('\n\n')
    if add_infinite_loops:
        rule_lines = rule_definitions.split('\n')
        for i in range(len(rule_lines)):
            if rule_lines[i].startswith('8:'):
                rule_lines[i] = '8: 42 | 42 8'
            elif rule_lines[i].startswith('11:'):
                rule_lines[i] = '11: 42 31 | 42 11 31'
        rule_definitions = '\n'.join(rule_lines)

    valid_messages = get_valid_messages(rule_definitions)

    return sum(
        does_message_match_rules(
            rules=rule_definitions,
            rule_num=rule_num,
            message=m,
            valid_messages=valid_messages
        )
        for m
        in messages.split('\n')
    )


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_messages_match_rule(puzzle_input)}")
    print(f"Part 2: {num_messages_match_rule(puzzle_input, add_infinite_loops=True)}")
