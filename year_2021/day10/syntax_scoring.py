from util import read_puzzle_input


CHUNK_COMPLETION_SCORES = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}
CHUNK_ERROR_SCORES = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
CHUNK_MAP = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<",
}
CHUNK_MAP_V2 = {
    open_chunk: close_chunk for close_chunk, open_chunk in CHUNK_MAP.items()
}
OPEN_CHUNKS = CHUNK_MAP.values()


def get_syntax_error_score(puzzle_input):
    lines = puzzle_input.split("\n")
    score = 0
    for line in lines:
        unmatched_open_chunks = []
        for ch in line:
            if ch in OPEN_CHUNKS:
                unmatched_open_chunks.append(ch)
            elif unmatched_open_chunks[-1] == CHUNK_MAP[ch]:
                unmatched_open_chunks.pop()
            else:
                score += CHUNK_ERROR_SCORES[ch]
                break

    return score


def get_median_completion_score(puzzle_input):
    lines = puzzle_input.split("\n")
    completion_scores = []

    for line in lines:
        is_corrupt = False
        unmatched_open_chunks = []
        for ch in line:
            if ch in OPEN_CHUNKS:
                unmatched_open_chunks.append(ch)
            elif unmatched_open_chunks[-1] == CHUNK_MAP[ch]:
                unmatched_open_chunks.pop()
            else:
                is_corrupt = True
                break
        if is_corrupt:
            continue
        score = 0
        while len(unmatched_open_chunks) > 0:
            next_char = CHUNK_MAP_V2[unmatched_open_chunks.pop()]
            score *= 5
            score += CHUNK_COMPLETION_SCORES[next_char]
        completion_scores.append(score)

    sorted_scores = sorted(completion_scores)
    return sorted_scores[len(completion_scores) // 2]


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_syntax_error_score(puzzle_input)}")
    print(f"Part 2: {get_median_completion_score(puzzle_input)}")
