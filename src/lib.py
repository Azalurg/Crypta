# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.2
# Date: 2023-28-01

import string
import random
import json
import os


class Library:
    def __init__(self, seed):
        self.__seed = seed
        if os.path.exists("./variables.json"):
            with open("./variables.json", "r") as f:
                variables = json.load(f)
                self.alphabet = variables["alphabet"]
                self.mixing = variables["bigger_primal"]
                self.divider = variables["big_primal"]
                self.amount = variables["amount"]
        else:
            self.alphabet = "abcdefghijklmnopqrstuvwxyz#"
            self.mixing = 6126031848641927606625849475313687769661220106449292634763085954973760603435362859797200428100659
            self.divider = 92774511385927202791711863005252216423819562473414722725889832461032494558329988063
            self.amount = 256

    def get_full_alphabet(self) -> str:
        return (
            string.ascii_uppercase
            + string.ascii_lowercase
            + string.digits
            + "!@#$%^&*(){}[]<>?\"'"
        )

    def get_seed(self):
        self.__seed = (self.__seed * self.mixing) % self.divider
        return self.__seed

    def pepper_alphabet(self):
        new_alphabet = []
        alphabet_copy = list(self.alphabet)
        while len(alphabet_copy) > 0:
            s = self.get_seed() % len(alphabet_copy)
            new_alphabet.append(alphabet_copy.pop(s))
        self.get_seed
        return new_alphabet

    def get_random_seed(self):
        self.__seed = (
            self.__seed * self.mixing + random.randint(0, self.divider - 1)
        ) % self.divider
        return self.__seed
