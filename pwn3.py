#!/usr/bin/env python3

# Importa la libreria di pwntools
from pwn import *

def main():

    elf = ELF("./sw-19")

    if args.REMOTE:
        p = remote("software-17.challs.olicyber.it", 13002)
    else:
        p = process([elf.path])

    p.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
    p.sendline(b"x")

    while(True):
        line = p.recvuntil(b':').decode().split()
        f_name = line[1].replace(":", "")
        addr = hex(elf.symbols[f_name])
        p.sendline(addr.encode())


    p.close()


if __name__ == "__main__":
    main()
