def rail_fence_encrypt(text, key):
    rail = [''] * key
    row, direction = 0, 1
    for char in text:
        rail[row] += char
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return ''.join(rail)

def rail_fence_decrypt(ciphertext, key):
    rail = [[''] * len(ciphertext) for _ in range(key)]
    row, direction, idx = 0, 1, 0
    for i in range(len(ciphertext)):
        rail[row][i] = '*'
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    for r in range(key):
        for c in range(len(ciphertext)):
            if rail[r][c] == '*':
                rail[r][c] = ciphertext[idx]
                idx += 1
    row, direction = 0, 1
    result = []
    for i in range(len(ciphertext)):
        result.append(rail[row][i])
        row += direction
        if row == 0 or row == key - 1:
            direction *= -1
    return ''.join(result)

# Example usage
plaintext = "HELLO WORLD"
key = 3
ciphertext = rail_fence_encrypt(plaintext.replace(" ", ""), key)
decrypted = rail_fence_decrypt(ciphertext, key)
print("Encrypted:", ciphertext)
print("Decrypted:", decrypted)
