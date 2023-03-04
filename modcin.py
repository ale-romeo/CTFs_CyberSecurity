def main():
    times = int(input("Inserisci numero di equazioni:"))
    y = [0]*times
    m = [0]*times
    M = [0]*times
    Minv = [0]*times
    x = 0
    mod = 1
    for _ in range(0, times):
        m[_] = int(input("Inserisci modulo:"))
        y[_] = int(input("Inserisci risultato:"))
        mod *= m[_]
    
    for _ in range(0, times):
        M[_] = mod//m[_]
        Minv[_] = pow(M[_], -1, m[_])
        x += y[_]*M[_]*Minv[_]
    
    modulo = int(input("Inserisci ultimo modulo:"))
    print(x % modulo)

if __name__ == "__main__":
    main()