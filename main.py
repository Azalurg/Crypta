# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.2
# Date: 2023-28-01

import sys

from src.oneTime import main as oneTime
from src.key import main as key
from src.password import main as password


def execute(decision: str):
    if decision == "1":
        oneTime()
    elif decision == "2":
        key()
    elif decision == "3":
        password()
    elif decision == "q":
        exit()
    else:
        print("Invalid input")


def main():
    if len(sys.argv) >= 2:
        execute(sys.argv[1])
    else:
        print("Welcome to Crypta!")
        while True:
            print("\n1. One time\n2. Generate key\n3. Password\nq. Exit\n")
            decision = input("Enter number: ")

            execute(decision)
            print("\n")


if __name__ == "__main__":
    main()
