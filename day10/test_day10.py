from day10 import knot_hash


def test_knot_hash():
    num_list = range(5)
    lengths = (3, 4, 1, 5)
    assert knot_hash(lengths=lengths, num_list=num_list) == 12
