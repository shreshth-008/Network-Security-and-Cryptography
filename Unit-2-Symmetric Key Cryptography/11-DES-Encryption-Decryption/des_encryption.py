from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

def encrypt(message, key):
    cipher = DES.new(key, DES.MODE_EAX)

    ciphertext, tag = cipher.encrypt_and_digest(message)

    return cipher.nonce, ciphertext, tag

def decrypt(ciphertext, key, nonce, tag):
    cipher = DES.new(key, DES.MODE_EAX, nonce=nonce)

    plaintext = cipher.decrypt_and_verify(ciphertext, tag)

    return plaintext


print("=== DES Encryption & Decryption ===")

message = input("Enter message: ").encode("utf-8")

key = get_random_bytes(8)

nonce, ciphertext, tag = encrypt(message, key)

decrypted = decrypt(ciphertext, key, nonce, tag)

print("\nOriginal Message :", message.decode("utf-8"))
print("Secret Key       :", key.hex())
print("Encrypted Message:", ciphertext.hex())
print("Decrypted Message:", decrypted.decode("utf-8"))