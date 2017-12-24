def is_valid_passphrase(passphrase):
    words = passphrase.split()
    return len(words) == len(set(words))
