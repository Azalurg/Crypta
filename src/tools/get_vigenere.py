def get_vigenere(alphabet: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"):
    matrix = {}

    for i, letter in enumerate(alphabet):
        matrix[letter] = i

    return matrix