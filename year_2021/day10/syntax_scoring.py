from collections import defaultdict

from util import read_puzzle_input


CHUNK_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
CHUNK_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
OPEN_CHUNKS = CHUNK_MAP.values()

def get_syntax_error_score(puzzle_input):
    lines = puzzle_input.split('\n')
    score = 0
    for line in lines:
        open_chunk_counts = defaultdict(int)
        for ch in line:
            if ch in OPEN_CHUNKS:
                open_chunk_counts[ch] += 1
            elif open_chunk_counts[CHUNK_MAP[ch]] > 0:
                open_chunk_counts[CHUNK_MAP[ch]] -= 1
            else:
                score += CHUNK_SCORES[ch]
                break

    return score


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_syntax_error_score(puzzle_input)}")
    print(f"Part 2: {get_syntax_error_score(puzzle_input)}")
