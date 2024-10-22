from Crypto.Cipher import ARC4
import itertools
import string

def rc4_decrypt(ciphertext, key):
    # Create a new RC4 cipher object with the provided key
    cipher = ARC4.new(key)
    return cipher.decrypt(ciphertext)

def brute_force_rc4(ciphertext, key_length):
    # Define a charset for brute-forcing (adjust depending on your key structure)
    charset = string.ascii_lowercase + string.ascii_uppercase + string.digits
    
    # Generate all possible key combinations of the specified length
    for key in itertools.product(charset, repeat=key_length):
        key = ''.join(key).encode('utf-8')
        decrypted_message = rc4_decrypt(ciphertext, key)
        
        # Check if the decrypted message makes sense (customize based on your knowledge)
        if b'secret' in decrypted_message:  # Replace 'known_text' with actual expected plaintext
            print(f'Found key: {key.decode("utf-8")}')
            print(f'Decrypted message: {decrypted_message.decode("utf-8")}')
            return key.decode('utf-8')
    
    return None

def main():
    # Get the ciphertext and key length from the user
    ciphertext = input('Enter the ciphertext in hexadecimal format: ')
    ciphertext = bytes.fromhex(ciphertext)
    key_length = int(input('Enter the key length: '))

    # Start brute-forcing with the specified key length
    found_key = brute_force_rc4(ciphertext, key_length)
    if found_key:
        print(f'Successfully found the key: {found_key}')
    else:
        print('Key not found.')
