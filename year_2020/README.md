Python packaging is confusing when you're trying to make it easy by not doing things the right way.

Scripts should be run from repo directory using the format `python -m year_2020.day01.expense_report` to make sure that the `util` module is available.

Tests can be run from anywhere (as far as I can tell) by running `pytest`.
