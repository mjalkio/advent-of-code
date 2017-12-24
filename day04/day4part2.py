from collections import Counter


def is_valid_anagram_passphrase(phrase):
    words = phrase.split()
    char_count_list = [Counter(word) for word in words]

    # Turn character counts into tuple-tuples so they can be hashed
    char_count_tuples = [tuple(sorted(c.items())) for c in char_count_list]

    return len(words) == len(set(char_count_tuples))
