from functools import reduce


def reverse_list(lst, start, length):
    for i in range(int(length / 2)):
        idx1 = (start + i) % len(lst)
        idx2 = (start + length - 1 - i) % len(lst)

        temp = lst[idx1]
        lst[idx1] = lst[idx2]
        lst[idx2] = temp
    return lst


def knot_hash(lengths, num_list):
    num_list, _, _ = hash_round(
        lengths=lengths, num_list=num_list, current_position=0, skip_size=0
    )
    return num_list[0] * num_list[1]


def hash_round(lengths, num_list, current_position, skip_size):
    for length in lengths:
        num_list = reverse_list(lst=num_list, start=current_position, length=length)
        current_position += (length + skip_size) % len(num_list)
        skip_size += 1
    return num_list, current_position, skip_size


def to_ascii(string):
    return [ord(char) for char in string]


def to_hex(numbers):
    return "".join([hex(num)[2:].zfill(2) for num in numbers])


def convert_input(string):
    return to_ascii(string) + [17, 31, 73, 47, 23]


def sparse_hash(lengths, num_list):
    current_position = 0
    skip_size = 0
    num_rounds = 64
    for _ in range(num_rounds):
        num_list, current_position, skip_size = hash_round(
            lengths=lengths,
            num_list=num_list,
            current_position=current_position,
            skip_size=skip_size,
        )
    return num_list


def xor(num_list):
    return reduce((lambda x, y: x ^ y), num_list)


def dense_hash(sparse_hash):
    if len(sparse_hash) != 256:
        raise ValueError("Invalid sparse hash provided.")
    dense_hash = []
    for i in range(16):
        start_idx = i * 16
        dense_hash.append(xor(sparse_hash[start_idx : start_idx + 16]))
    return dense_hash


def real_knot_hash(string):
    lengths = convert_input(string=string)
    sparse_hashing = sparse_hash(lengths=lengths, num_list=list(range(256)))
    dense_hashing = dense_hash(sparse_hash=sparse_hashing)
    return to_hex(dense_hashing)


if __name__ == "__main__":
    puzzle_input = "197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63"
    lengths = [int(length) for length in puzzle_input.split(",")]
    num_list = list(range(256))
    print("Part one: {hash}".format(hash=knot_hash(lengths=lengths, num_list=num_list)))
    print("Part two: {hash}".format(hash=real_knot_hash(puzzle_input)))
