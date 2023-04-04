from src.tools.get_key import get_key


def print_key():
    seed = int(input("Enter seed: "))
    key, seed = get_key(seed)

    for i in range(0, len(key)):
        print(key[i], end="")
        if (i + 1) % 32 == 0:
            print()