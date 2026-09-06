def encrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(
                (ord(char) - start + shift) % 26 + start
            )
            result += encrypted_char
            key_index += 1
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            start = ord('A') if char.isupper() else ord('a')

            decrypted_char = chr(
                (ord(char) - start - shift) % 26 + start
            )
            result += decrypted_char
            key_index += 1
        else:
            result += char

    return result

print("=== Vigenere Cipher ===")

message = input("Enter message: ")
key = input("Enter keyword: ")

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print("\nOriginal Message :", message)
print("Keyword          :", key.upper())
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)