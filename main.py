# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.1
# Date: 2023-04-01

from src.oneTime import main as oneTime
from src.key import main as key


def main():
    print("Welcome to Crypta!")

    while True:
        print("\n1. One time\n2. Generate key\n3. Exit\n")
        decision = input("Enter number: ")

        if decision == "1":
            oneTime()
        elif decision == "2":
            key()
        elif decision == "3":
            break
        else:
            print("Invalid input")

        print("\n")


if __name__ == "__main__":
    main()
