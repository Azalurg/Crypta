from src.tools.get_key import get_key
from src.tools.get_vigenere import get_vigenere


def quick_decryption():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ#"

    seed = int(input("Enter seed: "))
    encrypted_message = input("Enter encrypted message: ").upper()

    vigenere = get_vigenere(alphabet)
    key, seed = get_key(seed)

    decrypted_message = ""

    for i in range(len(encrypted_message)):
        lsum = abs(vigenere[key[i]] - vigenere[encrypted_message[i]])
        decrypted_message += alphabet[lsum]

    decrypted_message = decrypted_message.replace("#", " ").lower()
    print(decrypted_message)
