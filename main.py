# Author: Azalurg
# Project: Crypta
# Repository: www.github.com/Azalurg/crypta
# Version: 0.1
# Date: 2023-04-01

from src.print_key import print_key


def main():
    print("Welcome to Crypta!")

    while True:
        print("\n1. Generate key\n0. Exit\n")
        decision = input("Enter number: ")

        if decision == "1":
            print_key()

        elif decision == "0":
            break
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()
