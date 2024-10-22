from Crypto.Cipher import ARC4
import itertools
import binascii

def rc4_decrypt(ciphertext, key):
    # Create a new RC4 cipher object with the provided key
    cipher = ARC4.new(key)
    return cipher.decrypt(ciphertext)

def brute_force_rc4(ciphertext, key_length):
    # Define the charset for brute-forcing in hexadecimal (0-9, a-f)
    charset = '0123456789abcdef'
    
    # Generate all possible hexadecimal key combinations of the specified length
    for key in itertools.product(charset, repeat=key_length * 2):  # hex key is 2 chars per byte
        key_hex = ''.join(key)
        key_bytes = binascii.unhexlify(key_hex)  # Convert hex key to bytes
        decrypted_message = rc4_decrypt(ciphertext, key_bytes)
        
        # Check if the decrypted message contains something recognizable
        if b'secret area' in decrypted_message:  # Adjust this to match expected plaintext
            print(f'Found key: {key_hex}')
            print(f'Decrypted message: {decrypted_message.decode("utf-8", errors="ignore")}')
            return key_hex
    
    return None

def main():
    # Get the ciphertext and key length from the user
    ciphertext = input('Enter the ciphertext file: ')
    with open(ciphertext, 'rb') as f:
        ciphertext = f.read()
    key_length = int(input('Enter the key length: '))

    # Start brute-forcing with the specified key length
    found_key = brute_force_rc4(ciphertext, key_length)
    if found_key:
        print(f'Successfully found the key: {found_key}')
    else:
        print('Key not found.')

if __name__ == '__main__':
    main()
