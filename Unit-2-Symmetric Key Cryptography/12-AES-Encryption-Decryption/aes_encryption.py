from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


def encrypt(message, key):
    iv = get_random_bytes(16)

    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_message = pad(message, AES.block_size)

    ciphertext = cipher.encrypt(padded_message)

    return iv, ciphertext


def decrypt(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)

    padded_message = cipher.decrypt(ciphertext)

    message = unpad(padded_message, AES.block_size)

    return message


print("=== AES Encryption & Decryption ===")

message = input("Enter message: ").encode("utf-8")

key = get_random_bytes(16)

iv, ciphertext = encrypt(message, key)

decrypted = decrypt(ciphertext, key, iv)

print("\nOriginal Message :", message.decode("utf-8"))
print("Secret Key       :", key.hex())
print("IV               :", iv.hex())
print("Encrypted Message:", ciphertext.hex())
print("Decrypted Message:", decrypted.decode("utf-8"))