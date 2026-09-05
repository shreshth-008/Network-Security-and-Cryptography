def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            result += encrypted_char
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("=== Caesar Cipher ===")

message = input("Enter message: ")
shift = int(input("Enter shift value: "))

encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print("\nOriginal Message :", message)
print("Shift Value      :", shift)
print("Encrypted Message:", encrypted)
print("Decrypted Message:", decrypted)