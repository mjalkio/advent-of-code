from day10 import (convert_input, dense_hash, knot_hash, real_knot_hash,
                   sparse_hash, to_ascii, to_hex, xor)


def test_knot_hash():
    num_list = list(range(5))
    lengths = (3, 4, 1, 5)
    assert knot_hash(lengths=lengths, num_list=num_list) == 12


def test_to_ascii():
    string_input = '1,2,3'
    assert to_ascii(string_input) == [49, 44, 50, 44, 51]


def test_convert_input():
    string_input = '1,2,3'
    expected = [49, 44, 50, 44, 51, 17, 31, 73, 47, 23]
    assert convert_input(string_input) == expected


def test_hashes():
    # Just want to check that it runs...
    num_list = list(range(256))
    lengths = (3, 4, 1, 5)
    sparse_hashing = sparse_hash(lengths=lengths, num_list=num_list)
    dense_hash(sparse_hashing)


def test_xor():
    num_list = [65, 27, 9, 1, 4, 3, 40, 50, 91, 7, 6, 0, 2, 5, 68, 22]
    assert xor(num_list=num_list) == 64


def test_to_hex():
    num_list = [64, 7, 255]
    assert to_hex(numbers=num_list) == '4007ff'


def test_real_knot_hash():
    test_cases = (
        ('', 'a2582a3a0e66e6e86e3812dcb672a272'),
        ('AoC 2017', '33efeb34ea91902bb2f59c9920caa6cd'),
        ('1,2,3', '3efbe78a8d82f29979031a4aa0b16a9d'),
        ('1,2,4', '63960835bcdc130f0b66d7ff4f6a5a8e'),
    )

    for string, expected in test_cases:
        assert real_knot_hash(string=string) == expected
