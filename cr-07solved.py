import string
import base64

def encrypt(clear, key):
  enc = []
  for i in range(len(clear)):
    key_c = key[i % len(key)]
    enc_c = chr((ord(clear[i]) + ord(key_c)) % 128)
    enc.append(enc_c)
  return str(base64.urlsafe_b64encode("".join(enc).encode('ascii')), 'ascii')

def decrypt(enc, key):
    dec = []
    enc = str(base64.urlsafe_b64decode(enc.encode('ascii')), 'ascii')
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((128 + ord(enc[i]) - ord(key_c)) % 128)
        dec.append(dec_c)
    return "".join(dec)

def main():
    msg = "See you later in the city center"
    cipher = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="
    tab_enc, tab_dec = {}, {}

    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                for d in string.ascii_lowercase:
                    k1 = a+b+c+d

                    enc = encrypt(msg, k1)
                    tab_enc[enc] = k1

    for a in string.ascii_lowercase:
        for b in string.ascii_lowercase:
            for c in string.ascii_lowercase:
                for d in string.ascii_lowercase:
                    k2 = a+b+c+d

                    dec = decrypt(cipher, k2)
                    tab_dec[dec] = k2
                    if dec in tab_enc.keys():
                        print(tab_enc[dec]+k2)
        

if __name__ == "__main__":
    main()