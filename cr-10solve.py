from pwn import *

def main():
    r = remote("notadmin.challs.cyberchallenge.it", 9032)
    r.recvuntil(b'> ')
    user = ""
    msg = "usr=;is_admin=0"
    print(len(msg))
    r.sendline(b'1')
    r.recvuntil(b'username: ')
    r.sendline(user.encode())

    r.recvuntil(b'token: ')
    token = r.recvline().decode().strip()

    xor = ord('0') ^ ord('1')
    bit = token
    
    r.sendline(b'2')
    r.recvuntil(b'token: ')
    mod = token[:28] + hex(int(token[28:30], 16) ^ xor)[2:] + token[30:]
    r.sendline(mod.encode())
    r.recvuntil(b'> ')
        

if __name__ == "__main__":
    main()