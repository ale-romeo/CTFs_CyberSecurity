from pwn import *

def main():
    # connect to the server
    r = remote(b'software-17.challs.olicyber.it', 13000)
    r.recvuntil(b'... Invia un qualsiasi carattere per iniziare ...')
    r.sendline(b'x')

    # receive the array of numbers
    while(True):
        r.recvuntil(b'\n')
        data = r.recvuntil(b']')
        r.recvuntil(b':')
        # extract the numbers from the received data
        nums = list(map(int, data.decode("UTF-8").split('[')[1].split(']')[0].split(',')))
        
        # calculate the sum of the numbers
        result = sum(nums)
        result = str(result)

        # send the result back to the server
        r.sendline(result)

    # close the connection
    r.close()

if __name__ == '__main__':
    main()