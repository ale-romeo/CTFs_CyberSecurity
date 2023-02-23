from pwn import *

def rol_bytes(b):

    # Perform the shift operation
    for i in range(0, len(b)):
        print(b[i])
        b[i] = (b[i] << i) | (b[i] >> (8 - i))

    # Convert the bytearray back to a bytes object
    return bytes(b)


def main():
    # connect to the server
    b = bytearray(open('flag.txt.aes', 'rb').read())
    print(b)
    rol_bytes(b)
    res = b.decode()
    print(res)

if __name__ == '__main__':
    main()