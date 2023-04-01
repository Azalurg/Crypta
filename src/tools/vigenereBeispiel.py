alphabet = "abcdefghijklmnopqrstuvwxyz#"

k = 0


def add_key(key):
    key += 1
    key = key % len(alphabet)
    return key


with open("vigenereBeispiel.csv", "w") as f:
    f.write("*,")

    for l in alphabet:
        f.write(l + ",")

    f.write("\n")

    for i in range(len(alphabet)):
        f.write(alphabet[i] + ",")
        for j in range(len(alphabet)):
            f.write(alphabet[k] + ",")
            k = add_key(k)
        f.write("\n")
        k = add_key(k)
