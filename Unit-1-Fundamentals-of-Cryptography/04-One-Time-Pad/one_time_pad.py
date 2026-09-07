def encrypt(text, key):
    result = ""

    for i in range(len(text)):
        text_value = ord(text[i].upper()) - ord('A')
        key_value = ord(key[i].upper()) - ord('A')

        encrypted_value = (text_value + key_value) % 26
        encrypted_char = chr(encrypted_value + ord('A'))

        result += encrypted_char

    return result


def decrypt(ciphertext, key):
    result = ""

    for i in range(len(ciphertext)):
        cipher_value = ord(ciphertext[i]) - ord('A')
        key_value = ord(key[i].upper()) - ord('A')

        decrypted_value = (cipher_value - key_value) % 26
        decrypted_char = chr(decrypted_value + ord('A'))

        result += decrypted_char

    return result


print("=== One-Time Pad ===")

message = input("Enter message (letters only): ").upper()
key = input("Enter key (same length as message): ").upper()

if len(message) != len(key):
    print("Error: Key must be the same length as the message.")
else:
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)

    print("\nOriginal Message :", message)
    print("One-Time Key     :", key)
    print("Encrypted Message:", encrypted)
    print("Decrypted Message:", decrypted)