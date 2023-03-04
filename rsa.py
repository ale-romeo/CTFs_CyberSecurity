def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def main():
    a = int(input("Insert a:"))
    b = int(input("Insert b:"))
    mod = a*b
    phi = (a-1)*(b-1)

    print("Product is: ", mod)

    for _ in range(2, mod):
        g, x, y = gcdExtended(_, mod)
        if g == 1:
            msg = _
            break

    print("Message is: ", msg)
    print("Phi is: ", phi)

    for _ in range(2, phi):
        g, x, y = gcdExtended(_, phi)
        if g == 1:
            exp = _
            break
    
    print("Exponent is: ", exp)
    cipher = pow(msg, exp, mod)
    print("Ciphertext is: ", cipher)
    d = pow(exp, -1, phi)
    print("d is: ", d)

if __name__ == "__main__":
    main()