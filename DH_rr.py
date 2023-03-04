import math

def main():
    p = int(input("Insert p: "))
    g = int(input("Insert g: "))
    y = int(input("Insert y: "))

    for _ in range(y+1):
        result = pow(g, _, p)
        print("Result with", _, " is ", result)

if __name__ == "__main__":
    main()