from pwn import *
from string import printable

def main():
    r = remote("padding.challs.cyberchallenge.it", 9030)
    r.recvuntil(b'encrypt:')
    flag = ""

    for _ in range(31, 0, -1):
        msg = 'A'*_
        print(msg+flag)
        r.sendline(msg.encode())
        r.recvuntil(b'password: ')
        data = r.recvline().decode()[:64]
        r.recvline()

        for i in printable:
            tri = msg + flag + i
            r.recvuntil(b'encrypt:')
            r.sendline(tri.encode())
            r.recvuntil(b'password: ')
            hit = r.recvline().decode()[:64]
            r.recvline()
            if hit == data:
                flag = flag + i
                break



if __name__ == "__main__":
    main()