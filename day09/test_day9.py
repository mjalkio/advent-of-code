from day9part1 import score_stream


def test_score_stream():
    test_cases = (
        (r'{}', 1),
        (r'{{{}}}', 6),
        (r'{{},{}}', 5),
        (r'{{{},{},{{}}}}', 16),
        (r'{<a>,<a>,<a>,<a>}', 1),
        (r'{{<ab>},{<ab>},{<ab>},{<ab>}}', 9),
        (r'{{<!!>},{<!!>},{<!!>},{<!!>}}', 9),
        (r'{{<a!>},{<a!>},{<a!>},{<ab>}}', 3),
    )

    for puzzle_input, expected in test_cases:
        assert score_stream(puzzle_input) == expected
