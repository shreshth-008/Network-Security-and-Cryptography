import hashlib


def generate_mac(message, key):
    data = key + message
    data_bytes = data.encode("utf-8")

    hash_object = hashlib.sha256(data_bytes)
    mac = hash_object.hexdigest()

    return mac

print("=== Message Authentication Code (MAC) ===")

message = input("Enter message: ")
key = input("Enter secret key: ")

mac = generate_mac(message, key)

print("\nMessage   :", message)
print("Secret Key:", key)
print("MAC       :", mac)