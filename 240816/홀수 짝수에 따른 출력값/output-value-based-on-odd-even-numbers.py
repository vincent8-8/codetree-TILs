n = int(input())

def f(n):
    if n == 2 or n == 1:
        return n

    if n % 2 == 0:
        return f(n - 2) + n
    else:
        return f(n - 2) + n

print(f(n))