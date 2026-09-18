import time
import secrets

def create_request(message):
    nonce = secrets.token_hex(4)
    timestamp = time.time()

    return {
        "message": message,
        "nonce": nonce,
        "timestamp": timestamp
    }

def verify_request(request, used_nonces):
    nonce = request["nonce"]

    if nonce in used_nonces:
        return False

    used_nonces.add(nonce)
    return True

print("=== Replay Attack Demonstration & Prevention ===")

used_nonces = set()

request = create_request("Transfer Request")

print("\nOriginal Request:")
print("Message  :", request["message"])
print("Nonce    :", request["nonce"])

if verify_request(request, used_nonces):
    print("Status   : ACCEPTED")

print("\nReplayed Request:")

if verify_request(request, used_nonces):
    print("Status   : ACCEPTED")
else:
    print("Status   : REJECTED - Replay Attack Detected")