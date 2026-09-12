import hmac
import hashlib


def generate_hmac(message, key):
    message_bytes = message.encode("utf-8")
    key_bytes = key.encode("utf-8")

    hmac_object = hmac.new(
        key_bytes,
        message_bytes,
        hashlib.sha256
    )

    hmac_value = hmac_object.hexdigest()

    return hmac_value

print(" HMAC-SHA256 Implementation ")

message = input("Enter message: ")
key = input("Enter secret key: ")

hmac_value = generate_hmac(message, key)

print("\nOriginal Message :", message)
print("Secret Key       :", key)
print("HMAC-SHA256      :", hmac_value)
print("HMAC Length      :", len(hmac_value), "characters")