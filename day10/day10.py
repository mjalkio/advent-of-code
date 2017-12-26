def reverse_list(lst, start, length):
    idx = start % len(lst)
    for i in reversed(range(length)):
        temp = lst[idx]
        swap_idx = (idx + i) % len(lst)
        lst[idx] = lst[swap_idx]
        lst[swap_idx] = temp
        idx = (idx + 1) % len(lst)
    return lst


def knot_hash(lengths, num_list):
    current_position = 0
    skip_size = 0
    for length in lengths:
        num_list = reverse_list(lst=num_list,
                                start=current_position,
                                length=length)
        current_position += length + skip_size
        skip_size += 1
    return num_list[0] * num_list[1]
