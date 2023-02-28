from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import binascii

# Definizione dei parametri
key = get_random_bytes(32)
plaintext = 'Mi chiedo cosa significhi il numero nel nome di questo algoritmo.'
padding_scheme = 'pkcs7'
segment_size = 24

# Generazione di un vettore di inizializzazione casuale
iv = get_random_bytes(AES.block_size)

# Cifratura del testo
cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=segment_size)
padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size, padding_scheme)
ciphertext = cipher.encrypt(padded_plaintext)

# Stampa del risultato
print(key)
print('IV:', binascii.hexlify(iv))
print('Ciphertext:', binascii.hexlify(ciphertext))
