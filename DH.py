import math

def main():
    a = int(input("Insert base: "))
    b = int(input("Insert number: "))
    m = int(input("Insert module: "))

    for _ in range(b+1):
        result = pow(a, _, m)
        print("Result with", _, " is ", result)

if __name__ == "__main__":
    main()