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
    m = "See you later in the city center"
    c = "QSldSTQ7HkpIJj9cQBY3VUhbQ01HXD9VRBVYSkE6UWRQS0NHRVE3VUQrTDE="
    k1, k2 = "aaaa", "aaaa"
    find = False
    cant = list("aaaa")

    #itero caratteri in lowercase, assegnando il carattere iterato al i-semio carattere della seconda key
    for i in range(4):
        for _ in string.ascii_lowercase:
            if _ in cant[i]:
                continue
            k2 = list(k2)
            k2[i] = _
            k2 = "".join(k2)
            d = decrypt(c, k2)

            #provo a trovare un primo carattere per la prima key che dia come risultato il primo carattere di d
            for p in string.ascii_lowercase:
                k1 = list(k1)
                k1[i] = p
                k1 = "".join(k1)
                enc  = encrypt(m, k1)

                if enc[i] == d[i]:
                    print(enc, d)
                    find = True
                    break

            if find == True:
                find = False
                key = k1 + k2
                break
            if _ == 'z':
                i -= 1
                cant[i] += k2[i]
                print(cant)
        print(key)
    
    


if __name__ == "__main__":
    main()