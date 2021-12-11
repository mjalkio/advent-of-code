from util import read_puzzle_input


def get_num_easy_digit_outputs(puzzle_input):
    entries = puzzle_input.split("\n")

    num_easy_digits = 0
    for entry in entries:
        unique_patterns, output_digits = [
            digits.split(" ") for digits in entry.split(" | ")
        ]
        num_easy_digits += sum(len(d) in (2, 3, 4, 7) for d in output_digits)
    return num_easy_digits


def get_outputs_sum(puzzle_input):
    """
    Unique numbers are: 1 (2 segments), 4 (4 segments), 7 (3 segments), 8 (7 segments).
    5 segments: 2, 3, 5
    6 segments: 0, 6, 9

    My process to solve this (...there is probably an automated way to apply this logic)
    The segment that is in 7 but not in 1 is the A segment.
    The 6 can be identified as the number with only one of the segments from 1.
    The segment that is not in 6 but is in 1 is the C segment.
    The other segment in 1 is the F segment.
    The 3 is the only five segment number with the A, C, and F segments.
    Then 2 has an C and 5 has an F.
    ...sorry I stopped writing the process
    """
    entries = puzzle_input.split("\n")
    output_sum = 0
    for entry in entries:
        unique_patterns, output_patterns = [
            digits.split(" ") for digits in entry.split(" | ")
        ]
        unique_patterns = [set(pattern) for pattern in unique_patterns]
        output_patterns = [set(pattern) for pattern in output_patterns]

        identified_numbers = [None] * 10
        identified_segments = {}

        for pattern in unique_patterns:
            if len(pattern) == 2:
                identified_numbers[1] = pattern
            if len(pattern) == 4:
                identified_numbers[4] = pattern
            if len(pattern) == 3:
                identified_numbers[7] = pattern
            if len(pattern) == 7:
                identified_numbers[8] = pattern
        five_segment_numbers = [
            pattern for pattern in unique_patterns if len(pattern) == 5
        ]
        six_segment_numbers = [
            pattern for pattern in unique_patterns if len(pattern) == 6
        ]

        identified_segments["a"] = identified_numbers[7] - identified_numbers[1]
        for pattern in six_segment_numbers:
            if len(pattern) == 6 and len(identified_numbers[1] - pattern) == 1:
                identified_numbers[6] = pattern
                identified_segments["c"] = identified_numbers[1] - identified_numbers[6]
                identified_segments["f"] = (
                    identified_numbers[1] - identified_segments["c"]
                )
        for pattern in five_segment_numbers:
            if (
                len(
                    pattern
                    - identified_segments["a"]
                    - identified_segments["c"]
                    - identified_segments["f"]
                )
                == 2
            ):
                identified_numbers[3] = pattern
        for pattern in five_segment_numbers:
            if pattern == identified_numbers[3]:
                continue

            if len(pattern - identified_segments["c"]) == 4:
                identified_numbers[2] = pattern
                identified_segments["e"] = pattern - identified_numbers[3]
                identified_segments["f"] = identified_numbers[3] - pattern
            else:
                identified_numbers[5] = pattern
                identified_segments["b"] = pattern - identified_numbers[3]

        for pattern in six_segment_numbers:
            if pattern == identified_numbers[6]:
                continue

            if len(identified_segments["e"] - pattern) == 1:
                identified_numbers[9] = pattern
            else:
                identified_numbers[0] = pattern

        output_digits = [
            identified_numbers.index(pattern) for pattern in output_patterns
        ]
        output_value = "".join([str(digit) for digit in output_digits])
        output_sum += int(output_value)
    return output_sum


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_num_easy_digit_outputs(puzzle_input)}")
    print(f"Part 2: {get_outputs_sum(puzzle_input)}")
