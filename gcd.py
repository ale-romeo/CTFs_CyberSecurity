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
    a = int(input("Inserisci a:"))
    b = int(input("Inserisci b:"))
    g, x, y = gcdExtended(a, b)
    print(x, y)

    inv = int(input("Inserisci numero:"))
    mod = int(input("Inserisci modulo:"))
    g, x, y = gcdExtended(a, b)
    if g == 1:
        print("E' invertibile!")
    else:
        print("Non è invertibile.")
    
    inv = int(input("Inserisci numero:"))
    mod = int(input("Inserisci modulo:"))
    print(pow(inv, -1, mod))

if __name__ == "__main__":
    main()