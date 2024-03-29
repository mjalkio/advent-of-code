from math import prod

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


def hex_to_bin(binary_input):
    return "".join(HEX_TO_BIN_MAP[char] for char in binary_input)


def get_version_sum(puzzle_input):
    packet = hex_to_bin(puzzle_input)
    return handle_subpackets(packet)[0]


def _evaluate_operator(packet_type_id, subpackets):
    if packet_type_id == 0:
        return sum(subpackets)
    if packet_type_id == 1:
        return prod(subpackets)
    if packet_type_id == 2:
        return min(subpackets)
    if packet_type_id == 3:
        return max(subpackets)

    assert len(subpackets) == 2
    if packet_type_id == 5:
        return subpackets[0] > subpackets[1]
    if packet_type_id == 6:
        return subpackets[0] < subpackets[1]
    if packet_type_id == 7:
        return subpackets[0] == subpackets[1]

    raise ValueError("Invalid packet type ID")


def handle_subpackets(packet, num_subpackets=None):
    i = 0
    num_packets_parsed = 0
    version_sum = 0
    subpackets = []
    while i < len(packet):
        if all(char == "0" for char in packet[i:]):
            i = len(packet)
            continue

        if num_subpackets is not None and num_packets_parsed >= num_subpackets:
            return version_sum, subpackets, i

        num_packets_parsed += 1

        packet_version = packet[i : i + 3]
        version_sum += int(packet_version, 2)
        i += 3

        packet_type_id = int(packet[i : i + 3], 2)
        i += 3

        if packet_type_id == 4:
            # It's a literal
            literal_binary = ""
            have_hit_end_prefix = False
            while not have_hit_end_prefix:
                if packet[i] == "0":
                    have_hit_end_prefix = True
                i += 1
                literal_binary += packet[i : i + 4]
                i += 4
            subpackets.append(int(literal_binary, 2))
            continue

        # It's an operator
        length_type_id = packet[i]
        i += 1
        if length_type_id == "0":
            # the next 15 bits are a number that represents the total length
            # in bits of the sub-packets contained by this packet
            length = int(packet[i : i + 15], 2)
            i += 15
            subpackets_version_sum, op_subpackets, returned_length = handle_subpackets(
                packet[i : i + length]
            )
            assert length == returned_length
            version_sum += subpackets_version_sum
            i += returned_length
            # Now evaluate this and add it to subpackets
            subpackets.append(
                _evaluate_operator(
                    packet_type_id=packet_type_id, subpackets=op_subpackets
                )
            )
        else:
            # the next 11 bits are a number that represents the number
            # of sub-packets immediately contained by this packet
            num_sub_packets = int(packet[i : i + 11], 2)
            i += 11
            subpackets_version_sum, op_subpackets, returned_length = handle_subpackets(
                packet[i:], num_subpackets=num_sub_packets
            )
            version_sum += subpackets_version_sum
            i += returned_length
            # Now evaluate this and add it to subpackets
            subpackets.append(
                _evaluate_operator(
                    packet_type_id=packet_type_id, subpackets=op_subpackets
                )
            )

    return version_sum, subpackets, i


def evaluate_transmission(hex_input):
    packet = hex_to_bin(hex_input)
    return handle_subpackets(packet)[1][0]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_version_sum(puzzle_input)}")
    print(f"Part 2: {evaluate_transmission(puzzle_input)}")
