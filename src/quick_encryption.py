from src.tools.get_key import get_key
from src.tools.get_vigenere import get_vigenere


def quick_encryption():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"

    seed = int(input("Enter seed: "))
    message = input("Enter message: ").upper().replace(" ", "#")

    message_len = len(message)
    vigenere = get_vigenere(alphabet)
    key, seed = get_key(seed)

    encrypted_message = ""

    for i in range(len(key)):
        if message_len <= i:
            encrypted_message += key[i]
        else:
            lsum = (vigenere[key[i]] + vigenere[message[i]]) % len(alphabet)
            encrypted_message += alphabet[lsum]

    for i in range(len(encrypted_message)):
        print(encrypted_message[i], end="")
        if (i + 1) % 32 == 0:
            print()
