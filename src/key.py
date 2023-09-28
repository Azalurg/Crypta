# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.2
# Date: 2023-28-01

from src.lib import Library


def main():
    lib = Library(int(input("Enter seed: ")))

    key = ""

    for i in range(lib.amount):
        key += lib.alphabet[lib.get_seed() % len(lib.alphabet)]

    for i in range(0, len(key)):
        print(key[i], end="")
        if (i + 1) % 32 == 0:
            print()
