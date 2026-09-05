import string


def create_key():
    alphabet = string.ascii_uppercase
    key = input("Enter 26-letter substitution key: ").upper()

    if len(key) != 26 or set(key) != set(alphabet):
        raise ValueError("Key must contain all 26 letters exactly once.")

    return key


def encrypt(text, key):
    alphabet = string.ascii_uppercase
    result = ""

    for char in text:
        if char.isalpha():
            index = alphabet.index(char.upper())
            encrypted_char = key[index]

            if char.islower():
                encrypted_char = encrypted_char.lower()

            result += encrypted_char
        else:
            result += char

    return result


def decrypt(text, key):
    alphabet = string.ascii_uppercase
    result = ""

    for char in text:
        if char.isalpha():
            index = key.index(char.upper())
            decrypted_char = alphabet[index]

            if char.islower():
                decrypted_char = decrypted_char.lower()

            result += decrypted_char
        else:
            result += char

    return result


print("=== Monoalphabetic Substitution Cipher ===")

key = create_key()
message = input("Enter message: ")

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("\nOriginal Message :", message)
print("Substitution Key :", key)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)