from util import read_puzzle_input


def get_version_sum(puzzle_input):
    # Source: https://www.geeksforgeeks.org/python-ways-to-convert-hex-into-binary/
    transmission = "{0:08b}".format(int(puzzle_input, 16))

    version_sum = 0
    i = 0
    while i < len(transmission):
        packet_version = transmission[i : i + 3]
        version_sum += int(packet_version, 2)
        i += 3

        packet_type_id = int(transmission[i : i + 3], 2)
        i += 3

        if packet_type_id == 4:
            # It's a literal
            have_hit_end_prefix = False
            while not have_hit_end_prefix:
                if transmission[i] == "1":
                    have_hit_end_prefix = True
                i += 5
            continue

        # It's an operator
        if transmission[i] == "0":
            # the next 15 bits are a number that represents the total length
            # in bits of the sub-packets contained by this packet
            i += 1
            length = int(transmission[i : i + 15], 2)
            i += 15
        else:
            # the next 11 bits are a number that represents the number
            # of sub-packets immediately contained by this packet
            i += 1
            num_sub_packets = int(transmission[i : i + 11], 2)
            i += 11

    return version_sum


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_version_sum(puzzle_input)}")
    print(f"Part 2: {get_version_sum(puzzle_input)}")
