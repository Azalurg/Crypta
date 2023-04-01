# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.1
# Date: 2023-04-01

import json


def randomizer(seed: int, mixing: int, divider: int):
    return (seed * mixing) % divider


def main():
    with open('./variables.json', 'r') as f:
        variables = json.load(f)

    seed = int(input("Enter seed: "))

    key = ""

    for i in range(variables['amount']):
        seed = randomizer(seed, variables['bigger_primal'], variables['big_primal'])
        key += variables['alphabet'][seed % len(variables['alphabet'])]

    for i in range(0, len(key)):
        print(key[i], end="")
        if (i + 1) % 32 == 0:
            print()
