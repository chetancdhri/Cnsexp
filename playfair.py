def generate_key_matrix(key):
    key = ''.join(sorted(set(key.upper().replace('J', 'I')), key=lambda x: key.index(x)))
    alphabet = ''.join([chr(i) for i in range(65, 91) if i != ord('J')])
    key += ''.join([c for c in alphabet if c not in key])
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)

def playfair_encrypt_decrypt(text, matrix, encrypt=True):
    text = text.upper().replace('J', 'I').replace(' ', '')
    text += 'X' if len(text) % 2 else ''
    i = 0
    result = ""
    while i < len(text):
        a, b = text[i], text[i+1] if i+1 < len(text) else 'X'
        if a == b:
            b = 'X'
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        if row_a == row_b:
            result += matrix[row_a][(col_a + (1 if encrypt else -1)) % 5]
            result += matrix[row_b][(col_b + (1 if encrypt else -1)) % 5]
        elif col_a == col_b:
            result += matrix[(row_a + (1 if encrypt else -1)) % 5][col_a]
            result += matrix[(row_b + (1 if encrypt else -1)) % 5][col_b]
        else:
            result += matrix[row_a][col_b]
            result += matrix[row_b][col_a]
        i += 2
    return result

# Example usage
key = "PLAYFAIR EXAMPLE"
matrix = generate_key_matrix(key)
plaintext = "HIDETHEGOLDINTHETREX"
ciphertext = playfair_encrypt_decrypt(plaintext, matrix, encrypt=True)
decrypted_text = playfair_encrypt_decrypt(ciphertext, matrix, encrypt=False)

print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)
