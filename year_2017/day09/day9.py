import os.path as op

IGNORE_CHAR = "!"
GARBAGE_START_CHAR = "<"
GARBAGE_END_CHAR = ">"
GROUP_START_CHAR = "{"
GROUP_END_CHAR = "}"


def find_ignored_character_index(stream):
    return stream.find(IGNORE_CHAR)


def find_garbage_indices(stream):
    return stream.find(GARBAGE_START_CHAR), stream.find(GARBAGE_END_CHAR)


def remove_ignored_characters(stream):
    ignore_char_idx = find_ignored_character_index(stream)
    while ignore_char_idx != -1:
        stream = stream[:ignore_char_idx] + stream[ignore_char_idx + 2 :]
        ignore_char_idx = find_ignored_character_index(stream)
    return stream


def remove_garbage_blocks(stream):
    num_removed_chars = 0
    garbage_start_idx, garbage_end_idx = find_garbage_indices(stream)
    while garbage_start_idx != -1 and garbage_end_idx != -1:
        num_removed_chars += garbage_end_idx - garbage_start_idx - 1
        stream = stream[:garbage_start_idx] + stream[garbage_end_idx + 1 :]
        garbage_start_idx, garbage_end_idx = find_garbage_indices(stream)
    return stream, num_removed_chars


def score_stream(stream):
    stream = remove_ignored_characters(stream)
    stream, _ = remove_garbage_blocks(stream)

    # Finally go through the stream counting the score
    score = 0
    groups_started = 0
    for char in stream:
        if char == GROUP_START_CHAR:
            groups_started += 1
        if char == GROUP_END_CHAR and groups_started > 0:
            score += groups_started
            groups_started -= 1

    return score


def num_garbage_characters(stream):
    stream = remove_ignored_characters(stream)
    _, num_removed_chars = remove_garbage_blocks(stream)
    return num_removed_chars


if __name__ == "__main__":
    with open(op.join(op.dirname(__file__), "puzzle_input.txt"), "r") as f:
        puzzle_input = f.read()
    print("Stream score: {score}".format(score=score_stream(puzzle_input)))
    print(
        "Num garbage characters: {num}".format(num=num_garbage_characters(puzzle_input))
    )
