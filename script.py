from pwn import *
from string import printable

def main():
    r = remote("benchmark.challs.cyberchallenge.it", 9031)
    r.recvuntil(b":")
    flag = "CCIT{"
    r.sendline(flag)
    ans = r.recvuntil(b"cycles").decode().split()
    count = int(ans[4])
    r.recvuntil(b":")

    while True:
        for _ in printable:
            temp = flag + str(_)
            r.sendline(temp)
            ans = r.recvuntil(b"cycles").decode().split()
            tempcount = int(ans[4])
            print(tempcount, temp)
            flag = temp
            count = tempcount
            r.recvuntil(b":")


        r.recvuntil(b":")
        
    r.close()


if __name__ == "__main__":
    main()
