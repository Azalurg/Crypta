# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.2
# Date: 2023-28-01

import time
import hashlib
import os
from src.lib import Library


def main():
    password = ""
    sha256 = hashlib.sha256()
    path = os.path.expanduser("~/.zsh_history")

    with open(path, "rb") as f:
        while chunk := f.read(65536):
            sha256.update(chunk)

    seed = int(time.time()) + int.from_bytes(sha256.digest())
    lib = Library(seed)
    alphabet = lib.get_full_alphabet()
    alphabet_length = len(alphabet)

    length = int(input("Enter password len (default: 64): ") or "64")

    while len(password) < length:
        password += alphabet[lib.get_random_seed() % alphabet_length]

    print(password)
