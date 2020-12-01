from math import prod
from pathlib import Path


def sum_two_to_2020_product(expense_report_entries):
    """Find the product of the two entries in the expense report that sum to 2020."""
    for i, entry in enumerate(expense_report_entries):
        for j in range(i + 1, len(expense_report_entries)):
            if entry + expense_report_entries[j] == 2020:
                return entry * expense_report_entries[j]

    return None


def sum_three_to_2020_product(expense_report_entries):
    """Find the product of the three entries in the expense report that sum to 2020."""
    for i in range(len(expense_report_entries)):
        for j in range(i + 1, len(expense_report_entries)):
            for k in range(j + 1, len(expense_report_entries)):
                entries = (
                    expense_report_entries[i],
                    expense_report_entries[j],
                    expense_report_entries[k]
                )
                if sum(entries) == 2020:
                    return prod(entries)
    return None


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'puzzle01_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    expense_report_entries = [int(entry) for entry in puzzle_input.split('\n') if entry != '']
    print(f"Part 1: {sum_two_to_2020_product(expense_report_entries)}")
    print(f"Part 2: {sum_three_to_2020_product(expense_report_entries)}")
