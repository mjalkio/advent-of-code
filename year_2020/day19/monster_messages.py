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


def get_valid_messages(rule_definitions):
    rules_to_valid_messages = {}
    rules = _parse_rules(rule_definitions)
    while len(rules_to_valid_messages) < len(rules):
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
                        valid_messages_for_list = itertools.product(
                            valid_messages_for_list,
                            valid_messages_for_subrule
                        )
                valid_messages_for_rule = valid_messages_for_rule.union(valid_messages_for_list)
            rules_to_valid_messages[rule_num] = valid_messages_for_rule

    return rules_to_valid_messages


def does_message_match_rules(rules, rule_num, message):
    return None


def num_messages_match_rule(puzzle_input, rule_num=0):
    return None


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_messages_match_rule(puzzle_input)}")
    print(f"Part 2: {None}")
