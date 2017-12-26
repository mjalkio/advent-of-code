from day10 import convert_input, knot_hash, sparse_hash, to_ascii, xor


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


def test_sparse_hash():
    # Just want to check that it runs...
    num_list = range(5)
    lengths = (3, 4, 1, 5)
    sparse_hash(lengths=lengths, num_list=num_list)


def test_xor():
    num_list = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert xor(num_list=num_list) == 64
