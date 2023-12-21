from Crypto.Cipher import AES
from base64 import b64decode
import json

# The three strings provided
str1 = "a3c5a5a81ebc62c6144a9dc1ae5cce11"
str2 = "980daad49738f76b80c8fafb0673ff1b"
str3 = "fc78e6fee2138b798e1e51ed15e0a109"

# Function to XOR two hexadecimal strings
def xor_hex_strings(str1, str2):
    # Convert the hex strings to integers, XOR them, and then convert back to hex, padded with zeros if necessary
    xor_result = hex(int(str1, 16) ^ int(str2, 16))[2:].zfill(max(len(str1), len(str2)))
    return xor_result

# XOR the three strings together
partial_key = xor_hex_strings(str1, str2)
full_key_hex = xor_hex_strings(partial_key, str3)

# Convert the resulting hex string to bytes to be used as the AES key
key_bytes = bytes.fromhex(full_key_hex)

# Function to decrypt the message
def decrypt_message(file_path, key):
    with open(file_path, "rb") as f:
        try:
            data = json.loads(f.read())
            nonce = b64decode(data["nonce"])
            ciphertext = b64decode(data["ciphertext"])
            tag = b64decode(data["tag"])
            cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
            plaintext = cipher.decrypt_and_verify(ciphertext, tag)
            return "Decrypted message: " + plaintext.decode('utf-8')
        except (ValueError, KeyError) as e:
            return "Oops, something went wrong! " + str(e)

# Path to the encrypted message file
file_path = 'melding.enc'

# Attempt to decrypt the message
decrypted_message = decrypt_message(file_path, key_bytes)
print(decrypted_message)
