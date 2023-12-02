import itertools
from collections import defaultdict

from util import read_puzzle_input


def _parse_rules(rule_definitions):
    lines = [line for line in rule_definitions.split("\n") if line != ""]
    rules = defaultdict(list)
    for line in lines:
        rule_num_definition, definition = line.split(": ")
        rule_num = int(rule_num_definition)

        subrule_definitions = definition.split(" | ")
        for subrule_def in subrule_definitions:
            subrules = subrule_def.split(" ")
            rules[int(rule_num)].append(
                [int(subrule) if subrule.isdigit() else subrule for subrule in subrules]
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

            if not isinstance(subrule_lists[0][0], int):
                # If it's not a digit, it's a single character rule
                # Single character rules can be added immediately
                single_character_rule = subrule_lists[0][0]
                rules_to_valid_messages[rule_num] = {single_character_rule[1:-1]}
                continue

            # This rule depends on other rules
            all_required_subrules = [
                rule for subrule in subrule_lists for rule in subrule
            ]
            if not all(
                rule in rules_to_valid_messages.keys() for rule in all_required_subrules
            ):
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
                        valid_messages_for_list = set(
                            [
                                "".join(message_parts)
                                for message_parts in itertools.product(
                                    valid_messages_for_list, valid_messages_for_subrule
                                )
                            ]
                        )
                valid_messages_for_rule = valid_messages_for_rule.union(
                    valid_messages_for_list
                )
            rules_to_valid_messages[rule_num] = valid_messages_for_rule

        if num_rules_handled == len(rules_to_valid_messages):
            # No new rules were defined in this iteration.
            # This means we have infinite loops.
            # We'll handle this in the other methods...
            break
    return rules_to_valid_messages


def _get_possible_starts(message, rule_42_valid_messages):
    # These rules say that we have to start with rule 42 repeated as much as needed.
    possible_starts = set(
        [
            valid_message
            for valid_message in rule_42_valid_messages
            if message.startswith(valid_message)
        ]
    )

    while True:
        num_possible_starts_defined = len(possible_starts)
        new_possible_starts = set(
            [
                "".join(message_parts)
                for message_parts in itertools.product(
                    possible_starts, rule_42_valid_messages
                )
                if message.startswith("".join(message_parts))
            ]
        )
        possible_starts = possible_starts.union(new_possible_starts)
        if len(possible_starts) == num_possible_starts_defined:
            # There aren't more possibilities to determine
            break
        num_possible_starts_defined = len(possible_starts)
    return possible_starts


def _get_possible_endings(message, rule_31_valid_messages):
    possible_endings = set()
    i = 1
    while True:
        new_possible_endings = {""}
        for _ in range(i):
            new_possible_endings = set(
                [
                    "".join(message_parts)
                    for message_parts in itertools.product(
                        rule_31_valid_messages, new_possible_endings
                    )
                    if message.endswith("".join(message_parts))
                ]
            )

        if len(new_possible_endings) == 0:
            break
        for new_possible_ending in new_possible_endings:
            possible_endings.add((new_possible_ending, i))
        i += 1
    return possible_endings


def _get_possible_endings_with_middles(
    message, possible_endings, rule_42_valid_messages
):
    possible_endings_with_middles = set()
    for possible_ending, num_42s_to_add in possible_endings:
        new_possible_endings = {possible_ending}
        for _ in range(num_42s_to_add):
            new_possible_endings = set(
                [
                    "".join(message_parts)
                    for message_parts in itertools.product(
                        rule_42_valid_messages, new_possible_endings
                    )
                    if message.endswith("".join(message_parts))
                ]
            )

        possible_endings_with_middles = possible_endings_with_middles.union(
            new_possible_endings
        )
    return possible_endings_with_middles


def does_message_match_rules(rules, rule_num, message, valid_messages=None):
    if valid_messages is None:
        # It takes time to get valid messages, allow us to calculate once
        valid_messages = get_valid_messages(rules)

    if rule_num in valid_messages:
        return message in valid_messages[rule_num]

    # This situation occurs when we have infinite loops in the definition.
    # We happen to know this only affects three rules in our inputs.
    # 0: 8 11
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    # So really the question is if we can make the message with these rules.

    possible_starts = _get_possible_starts(
        message=message,
        rule_42_valid_messages=valid_messages[42],
    )

    if len(possible_starts) == 0:
        return False

    # Now we need to see if we can end it with rule 11. It takes forms like this:
    # 42 31
    # 42 42 31 31
    # 42 42 42 31 31 31
    # Here we start backwards and find possible endings.
    possible_endings = _get_possible_endings(
        message=message,
        rule_31_valid_messages=valid_messages[31],
    )

    if len(possible_endings) == 0:
        return False

    # For each of these possible endings we need to see if we can add 42s
    possible_endings_with_middles = _get_possible_endings_with_middles(
        message=message,
        possible_endings=possible_endings,
        rule_42_valid_messages=valid_messages[42],
    )

    for possible_start in possible_starts:
        for possible_ending in possible_endings_with_middles:
            if f"{possible_start}{possible_ending}" == message:
                return True

    return False


def num_messages_match_rule(puzzle_input, add_infinite_loops=False, rule_num=0):
    rule_definitions, messages = puzzle_input.split("\n\n")
    if add_infinite_loops:
        rule_lines = rule_definitions.split("\n")
        for i in range(len(rule_lines)):
            if rule_lines[i].startswith("8:"):
                rule_lines[i] = "8: 42 | 42 8"
            elif rule_lines[i].startswith("11:"):
                rule_lines[i] = "11: 42 31 | 42 11 31"
        rule_definitions = "\n".join(rule_lines)

    valid_messages = get_valid_messages(rule_definitions)

    return sum(
        does_message_match_rules(
            rules=rule_definitions,
            rule_num=rule_num,
            message=m,
            valid_messages=valid_messages,
        )
        for m in messages.split("\n")
    )


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {num_messages_match_rule(puzzle_input)}")
    print(f"Part 2: {num_messages_match_rule(puzzle_input, add_infinite_loops=True)}")
