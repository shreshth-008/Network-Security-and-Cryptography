import hashlib


def calculate_sha256(message):
    message_bytes = message.encode("utf-8")

    sha256 = hashlib.sha256()

    sha256.update(message_bytes)

    hash_value = sha256.hexdigest()

    return hash_value

print("=== SHA-256 Hash Function ===")

message = input("Enter message: ")

hash_value = calculate_sha256(message)

print("\nOriginal Message :", message)
print("SHA-256 Hash     :", hash_value)
print("Hash Length      :", len(hash_value), "characters")