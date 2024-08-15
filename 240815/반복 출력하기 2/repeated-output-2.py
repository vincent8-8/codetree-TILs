n = int(input())

def print_Hello(n):
    if n == 0:
        return
    print_Hello(n-1)
    print("HelloWorld")

print_Hello(n)