# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.2
# Date: 2023-28-01

from src.lib import Library


def main():
    lib = Library(int(input("Enter seed: ")))

    one_line_len = len("000. {}".format(" | ".join(lib.pepper_alphabet())))
    line = "\n" + "".join("-" for i in range(one_line_len)) + "\n"

    for i in range(lib.amount):
        print("{:03d}. {}".format(i + 1, " | ".join(lib.pepper_alphabet())), end=line)
