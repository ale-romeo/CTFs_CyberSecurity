#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

def main():

    p = remote(b"piecewise.challs.cyberchallenge.it", 9110)
        
    while(True):
        line = p.recvline().decode().split()
        if line[4] == "empty":
            p.sendline()
        else:
            bit = int(line[5])
            if line[8] == "64-bit":
                if line[9] == "little-endian":
                    res = p64(bit, endian = 'little')
                if line[9] == "big-endian":
                    res = p64(bit, endian = 'big')
            if line[8] == "32-bit":
                if line[9] == "little-endian":
                    res = p32(bit, endian = 'little')
                if line[9] == "big-endian":
                    res = p32(bit, endian = 'big')
            p.send(res)
        p.recvline()

    p.close()


if __name__ == "__main__":
    main()