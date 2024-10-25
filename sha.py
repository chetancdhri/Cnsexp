import hashlib

def sha512_hash(text):
    # Create a SHA-512 hash object
    sha512 = hashlib.sha512()
    
    # Update the hash object with the bytes of the input text
    sha512.update(text.encode('utf-8'))
    
    # Return the hexadecimal digest of the hash
    return sha512.hexdigest()

# Example usage
text = "Hello, world!"
hashed_text = sha512_hash(text)
print("Original Text:", text)
print("SHA-512 Hash:", hashed_text)
