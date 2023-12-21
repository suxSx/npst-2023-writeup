def char_map(text):
    char_dict = {}
    for index, char in enumerate(text):
        if char in char_dict:
            char_dict[char].append(index)
        else:
            char_dict[char] = [index]
    return char_dict

def decrypt_text(code, text):
    import ast
    indices = ast.literal_eval(code)
    return ''.join([text[index] for index in indices])

# Example usage
# decrypted_text = decrypt_text(code_txt, nissetekst)