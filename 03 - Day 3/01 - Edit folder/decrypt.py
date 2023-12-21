import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii

# Function to decrypt the file
def decrypt_aes_192_cbc(file_path, key_hex, iv):
    # Convert hex key to bytes
    key = binascii.unhexlify(key_hex)

    # Initialize the AES Cipher in CBC mode
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv.encode()), backend=default_backend())

    # Read the encrypted file
    with open(file_path, 'rb') as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the data
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data)

    return decrypted_data


# Key and IV
key_hex = 'dda2846b010a6185b5e76aca4144069f88dc7a6ba49bf128'
iv = 'UtgangsVektor123'

# File path
file_path = 'huskeliste.txt.enc'

# Perform decryption
try:
    decrypted_data = decrypt_aes_192_cbc(file_path, key_hex, iv)
    print("Decryption successful. Decrypted content:")
    print(decrypted_data)
except Exception as e:
    print("Decryption failed:", e)
