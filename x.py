from pwn import p8

def main():
    secret_command = p8(0x3f)
    payload = secret_command+p8(0x00)+p8(0x00)

    '''rs = list()
    start = 0x00
    for _ in range(0, 64):
        rs.append(p8(start))
        start += 1

    for _ in range(0, 32):
        payload += copy+rs[_]+rs[_+32]'''

    print(payload)

    with open('program.bin', 'wb') as f:
        f.write(payload)


if __name__ == '__main__':
    main()