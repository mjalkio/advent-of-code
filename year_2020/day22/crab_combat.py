from collections import deque

from util import read_puzzle_input


def _get_decks(puzzle_input):
    lines = [line for line in puzzle_input.split('\n') if line != '']
    deck = deque()
    for line in lines:
        if line == 'Player 1:':
            continue
        if line == 'Player 2:':
            p1_deck = deck
            deck = deque()
            continue

        deck.append(int(line))

    return p1_deck, deck


def get_winning_combat_score(puzzle_input, recursive=True):
    p1_deck, p2_deck = _get_decks(puzzle_input)

    while len(p1_deck) > 0 and len(p2_deck) > 0:
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()

        if p1_card > p2_card:
            p1_deck.append(p1_card)
            p1_deck.append(p2_card)
        else:
            p2_deck.append(p2_card)
            p2_deck.append(p1_card)

    winner_deck = p1_deck if len(p1_deck) > 0 else p2_deck
    score = 0
    for i in range(len(winner_deck)):
        score += (len(winner_deck) - i) * winner_deck[i]
    return score


if __name__ == '__main__':
    puzzle_input = read_puzzle_input()

    print(f"Part 1: {get_winning_combat_score(puzzle_input)}")
    print(f"Part 2: {get_winning_combat_score(puzzle_input, recursive=True)}")
