from collections import Counter, namedtuple
from enum import Enum
from functools import cmp_to_key

from util import read_puzzle_input


CHARACTERS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

Play = namedtuple("Play", ["hand", "bid"])


class HandType(Enum):
    FIVE_OF_KIND = 1
    FOUR_OF_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7


def _get_hand_type(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return HandType.FIVE_OF_KIND

    if 4 in counts.values():
        return HandType.FOUR_OF_KIND

    if 3 in counts.values():
        if 2 in counts.values():
            return HandType.FULL_HOUSE
        return HandType.THREE_OF_KIND

    if 2 in counts.values():
        if len(counts) == 3:
            return HandType.TWO_PAIR
        return HandType.ONE_PAIR

    return HandType.HIGH_CARD


def _compare_hands(a, b):
    if a == b:
        return 0

    a_type = _get_hand_type(a.hand)
    b_type = _get_hand_type(b.hand)

    if a_type == b_type:
        for a_char, b_char in zip(a.hand, b.hand):
            if a_char == b_char:
                continue
            if CHARACTERS.index(a_char) > CHARACTERS.index(b_char):
                return 1
            return -1

    if a_type.value > b_type.value:
        return -1

    return 1


def get_total_winnings(puzzle_input):
    lines = [line.split(" ") for line in puzzle_input.split("\n")]
    plays = [Play(hand=line[0], bid=int(line[1])) for line in lines]
    plays.sort(key=cmp_to_key(_compare_hands))
    return sum(play.bid * (rank + 1) for rank, play in enumerate(plays))


if __name__ == "__main__":
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_total_winnings(puzzle_input)}")
    print(f"Part 2: {get_total_winnings(puzzle_input)}")
