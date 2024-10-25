import numpy as np

# Hill Cipher Encryption
def hill_encrypt_decrypt(text, key_matrix, encrypt=True):
    n = len(key_matrix)
    text = text.replace(" ", "").upper()
    padding_len = n - len(text) % n if len(text) % n != 0 else 0
    text += 'X' * padding_len
    
    text_vector = [ord(char) - ord('A') for char in text]
    chunks = [text_vector[i:i + n] for i in range(0, len(text_vector), n)]
    
    if not encrypt:
        key_matrix = mod_inv_matrix(key_matrix)
    
    result = ""
    for chunk in chunks:
        result_matrix = np.dot(key_matrix, chunk) % 26
        result += ''.join(chr(num + ord('A')) for num in result_matrix)
    
    return result

# Find modular inverse matrix
def mod_inv_matrix(matrix):
    det = int(np.round(np.linalg.det(matrix))) % 26
    det_inv = mod_inverse(det, 26)
    return (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % 26

# Modular inverse of determinant
def mod_inverse(a, m):
    return next(x for x in range(1, m) if (a * x) % m == 1)

# Example usage
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
plaintext = "HELLO"
ciphertext = hill_encrypt_decrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)
print("Decrypted:", hill_encrypt_decrypt(ciphertext, key_matrix, encrypt=False))
