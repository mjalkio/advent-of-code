from day10 import convert_input, knot_hash, to_ascii


def test_knot_hash():
    num_list = range(5)
    lengths = (3, 4, 1, 5)
    assert knot_hash(lengths=lengths, num_list=num_list) == 12


def test_to_ascii():
    string_input = '1,2,3'
    assert to_ascii(string_input) == [49, 44, 50, 44, 51]


def test_convert_input():
    string_input = '1,2,3'
    expected = [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    assert convert_input(string_input) == expected
