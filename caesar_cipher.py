from sys import exit


def encrypt_caesar(text_input, shift):
    """Encrypts a message using the Caesar cipher technique."""

    capitals = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                "U", "V", "W", "X", "Y", "Z"]

    lowercase = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

    alphabet_len = len(capitals)

    encrypted = ""

    for char in text_input:
        try:
            if char.isupper():
                # The remainder will always be between 0 and alphabet_len - 1
                new_char = (capitals.index(char) + shift) % alphabet_len
                encrypted += capitals[new_char]
            elif char.islower():
                new_char = (lowercase.index(char) + shift) % alphabet_len
                encrypted += lowercase[new_char]
            # Spaces are not encrypted
            elif char == " ":
                encrypted += " "
            # Numbers are not encrypted as well
            else:
                encrypted += char
        # Unsupported letters with a diacritical mark
        except ValueError:
            print(
                f"The character '{char}' is not supported."
                "\nPlease, try a different message."
            )
            exit()

    return encrypted


print("Do you want to encrypt or decrypt your text using the Caesar cipher?")

# The prompt is repeated until the user chooses E/D (or e/d)
while True:
    encrypt_decrypt = input("\nType E to encrypt or D to decrypt: ").upper()

    if encrypt_decrypt not in ("E", "D"):
        print("\nWrong input.")
        continue
    break


message = input("\nType in the message:\n")

# Different messages for encryption and decryption
if encrypt_decrypt == "E":
    print(
        "\nShift by how many positions? "
        "Type in a positive integer to shift right, "
        "negative for a left shift."
    )
else:
    print(
        "\nBy how many positions was the original message shifted?"
        "\nIf you don't know, type in '0' (zero)."
    )

# Is the shift parameter an integer?
while True:
    try:
        shift_param = int(input())
    except ValueError:
        print(
            "\nIncorrect input. "
            "The shift parameter needs to be an integer."
            "\nPlease, try again."
        )
        continue
    break

# Apply the function to all three cases (encrypt, decrypt and decrypt unknown)
if encrypt_decrypt == "E":
    encrypted_text = encrypt_caesar(message, shift_param)
    print(
        "\nThe encrypted text is:"
        f"\n{encrypted_text}"
    )
# Decryption with an unknown shift parameter
elif shift_param == 0:
    print("\nHere are all the possibilities for a standard Latin alphabet:\n")
    for n in range(1, 26):
        decrypted_text = encrypt_caesar(message, -n)
        print(f"Shift {n}:", decrypted_text)
# Decryption with a given shift parameter
else:
    decrypted_text = encrypt_caesar(message, -shift_param)
    print(
        "\nThe decrypted text is:"
        f"\n{decrypted_text}"
    )
