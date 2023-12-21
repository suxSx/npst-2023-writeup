
def reverse_explode(encrypted_text, otp):
    # Calculate the size of each fragment
    fragment_size = len(encrypted_text) // len(otp)
    
    # Reverse the order of the fragments based on otp
    reordered_fragments = [''] * len(otp)
    for i, pos in enumerate(otp):
        start_index = pos * fragment_size
        end_index = start_index + fragment_size
        reordered_fragments[i] = encrypted_text[start_index:end_index]

    # Reassemble the original text and reverse the character shift
    original_text = ''.join(reordered_fragments)
    original_text = ''.join([chr(ord(c) - 2) for c in original_text])

    return original_text

# OTP list from pinneved.py
otp = [23, 2, 0, 5, 13, 16, 22, 7, 9, 4, 19, 21, 18, 10, 20, 11, 12, 14, 6, 1, 3, 8, 17, 15]

# Read the content of 'pinneved.txt'
with open('pinneved.txt', 'r') as file:
    encrypted_text = file.read()

# Apply the reverse function to the encrypted text
original_content = reverse_explode(encrypted_text, otp)
print(original_content)

# Save the original content to 'decrypted.txt'
#with open('decrypted.txt', 'w') as file:
#    file.write(original_content)
