# Caesar Cipher Encryption
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

# Caesar Cipher Decryption
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

# Example usage
text = "Hello, World!"
shift = 3

# Encrypting the text
encrypted = encrypt(text, shift)
print("Encrypted:", encrypted)

# Decrypting the text
decrypted = decrypt(encrypted, shift)
print("Decrypted:", decrypted)
