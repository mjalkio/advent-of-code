from pathlib import Path


def sum_to_2020_product(expense_report_entries):
    """Find the product of the two entries in the expense report that sum to 2020."""
    for i, entry in enumerate(expense_report_entries):
        for j in range(i + 1, len(expense_report_entries)):
            if entry + expense_report_entries[j] == 2020:
                return entry * expense_report_entries[j]

    return None


if __name__ == '__main__':
    puzzle_input_path = Path(Path(__file__).parent, 'puzzle01_input.txt')
    with puzzle_input_path.open() as f:
        puzzle_input = f.read()

    expense_report_entries = [int(entry) for entry in puzzle_input.split('\n') if entry != '']
    print(sum_to_2020_product(expense_report_entries))
