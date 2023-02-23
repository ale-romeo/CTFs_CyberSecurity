from pwn import *

def rol_bytes(b):

    # Perform the shift operation
    for i in range(len(b)):
        shift = i + 1
        b[i] = ((b[i] << shift) & 0xff) | (b[i] >> (8 - shift))
        print(shift, b[i])


def main():
    # connect to the server
    b = bytearray(open('flag.txt.aes', 'rb').read())
    rol_bytes(b)
    flag = bytes(b)
    print(flag)
    

if __name__ == '__main__':
    main()
