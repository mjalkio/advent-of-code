from util import read_puzzle_input


HEX_TO_BIN_MAP = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def _get_version_sum(packet, num_packets=None):
    version_sum = 0
    i = 0
    num_packets_parsed = 0
    while i < len(packet):
        if len(packet[i:]) < 6:
            # Not enough bits for a header, these are probably trailing 0s
            assert all(char == "0" for char in packet[i:])
            i = len(packet)
            continue

        if num_packets is not None and num_packets_parsed >= num_packets:
            return version_sum, i

        packet_version = packet[i : i + 3]
        version_sum += int(packet_version, 2)
        i += 3

        packet_type_id = int(packet[i : i + 3], 2)
        i += 3

        if packet_type_id == 4:
            # It's a literal
            have_hit_end_prefix = False
            while not have_hit_end_prefix:
                if packet[i] == "0":
                    have_hit_end_prefix = True
                i += 5
            continue

        # It's an operator
        length_type_id = packet[i]
        i += 1
        if length_type_id == "0":
            # the next 15 bits are a number that represents the total length
            # in bits of the sub-packets contained by this packet
            length = int(packet[i : i + 15], 2)
            i += 15
            version_sum += _get_version_sum(packet[i : i + length])[0]
            i += length
        else:
            # the next 11 bits are a number that represents the number
            # of sub-packets immediately contained by this packet
            num_sub_packets = int(packet[i : i + 11], 2)
            i += 11
            subpackets_version_sum, subpackets_i = _get_version_sum(
                packet[i:], num_packets=num_sub_packets
            )
            i += subpackets_i
            version_sum += subpackets_version_sum

        num_packets_parsed += 1
    return version_sum, i


def hex_to_bin(binary_input):
    return "".join(HEX_TO_BIN_MAP[char] for char in binary_input)


def get_version_sum(puzzle_input):
    packet = hex_to_bin(puzzle_input)
    return _get_version_sum(packet)[0]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_version_sum(puzzle_input)}")
    print(f"Part 2: {get_version_sum(puzzle_input)}")
