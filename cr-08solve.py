from Crypto.Cipher import AES
import binascii, sys
from string import printable

def main():
    key = "yn9RB3Lr43xJK2"
    iv = ""
    cipher = "c5██████████████████████████d49e78c670cb67a9e5773d696dc96b78c4e0"
    msg = "AES with CBC is very unbreakable".encode()

    cipher_blocks = [cipher[i:i+32] for i in range(0, len(cipher), 32)]
    msg_blocks = [msg[i:i+16] for i in range(0, len(msg), 16)]
    
    cipher_blocks[1] = binascii.unhexlify(cipher_blocks[1])
    cipher_block0 = "c5 00 00 00 00 00 00 00 00 00 00 00 00 00 d4 9e".split(" ")
    print(cipher_block0, msg_blocks[1])

    for a in printable:
        for b in printable:
            k = (key + a + b).encode()

            for hex1 in range(0, 255):
                aes = AES.new(key, AES.MODE_CBC, iv)
                print (binascii.hexlify(aes.encrypt(msg)).decode())



if __name__ == "__main__":
    main()