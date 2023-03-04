from pwn import *

def main():

    p = remote(b"crypto-08.challs.olicyber.it", 30001)
    p.recvuntil(b"lupo!\n")

    while(True):
        p.recvline()
        line = p.recvuntil(b"?").decode().split()
        print(line)
        if line[1] == '%':
            result = int(line[0])%int(line[2])
            p.sendline(str(result).encode())
            p.recvuntil(b'\n')
        if line[1] == "==":
            p.recvuntil(b")")
            mod1 = int(line[0]) % int(line[4].replace(")", "").replace("?", ""))
            mod2 = int(line[2]) % int(line[4].replace(")", "").replace("?", ""))
            print(mod1, mod2)
            if mod1 == mod2:
                p.sendline(b"si")
            else:
                p.sendline(b"no")
            p.recvall()
            break
            
    p.close()


if __name__ == "__main__":
    main()