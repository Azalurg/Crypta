# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.1
# Date: 2023-04-01

import json


def randomizer(seed: int, mixing: int, divider: int):
    return (seed * mixing) % divider


def prepper_alphabet(seed: int, alphabet: list, mixing: int, divider: int):
    new_alphabet = []
    alphabet_copy = list(alphabet)
    for letter in alphabet:
        s = randomizer(seed, mixing, divider) % len(alphabet_copy)
        new_alphabet.append(alphabet_copy[s])
        alphabet_copy.pop(s)
        seed = randomizer(seed, mixing, divider)
    return new_alphabet, seed


def main():
    with open('./variables.json', 'r') as f:
        variables = json.load(f)

    seed = int(input("Enter seed: "))

    for i in range(variables['amount']):
        new_alphabet, seed = prepper_alphabet(seed, variables['alphabet'], variables['bigger_primal'], variables['big_primal'])
        print("{:03d}. {}".format(i+1, " | ".join(new_alphabet)))
