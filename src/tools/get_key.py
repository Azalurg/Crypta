from src.tools.get_seed import get_seed


def get_key(seed: int, key_len: int = 256, alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"):
    key = ""
    s = seed
    for i in range(key_len):
        s = get_seed(s)
        key += alphabet[s % len(alphabet)]
    return key, s
