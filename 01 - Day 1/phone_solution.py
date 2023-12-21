def decrypt_message(encoded_message):
    # Mapping of numbers to letters as per old phone keypad
    keypad = {
        '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
        '6': 'MNO', '7': 'PQRS', '8': 'TUV', '9': 'WXYZ',
        '0': ' '  # Space for '0'
    }

    # Splitting the encoded message into pairs
    pairs = encoded_message.split()

    # Decoding each pair
    decoded_message = ''
    for pair in pairs:
        digit, count = pair.split('-')
        if digit in keypad:
            # The count in the pair is 1-based, so subtract 1 for 0-based indexing
            letter_index = int(count) - 1
            decoded_message += keypad[digit][letter_index]
        else:
            # If the digit is not in the keypad (like '1'), we can ignore or handle it differently
            pass

    return decoded_message


# Example input
input_message = "7-4 9-3 7-4 8-1 3-2 6-1 0-1 4-3 6-2 3-3 4-3 7-4 3-2 7-3 8-1 0-1 4-1 7-3 8-2 6-2 5-2 3-2 7-3 0-1 4-3 6-2 2-3 6-3 6-1 4-3 6-2 4-1"

print(decrypt_message(input_message))
