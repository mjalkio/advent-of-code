def reverse_list(lst, start, length):
    for i in range(length / 2):
        idx1 = (start + i) % len(lst)
        idx2 = (start + length - 1 - i) % len(lst)

        temp = lst[idx1]
        lst[idx1] = lst[idx2]
        lst[idx2] = temp
    return lst


def knot_hash(lengths, num_list):
    current_position = 0
    skip_size = 0
    for length in lengths:
        num_list = reverse_list(lst=num_list,
                                start=current_position,
                                length=length)
        current_position += (length + skip_size) % len(num_list)
        skip_size += 1
    return num_list[0] * num_list[1]

if __name__ == '__main__':
    puzzle_input = '197,97,204,108,1,29,5,71,0,50,2,255,248,78,254,63'
    lengths = [int(length) for length in puzzle_input.split(',')]
    num_list = range(256)
    print(knot_hash(lengths=lengths, num_list=num_list))
