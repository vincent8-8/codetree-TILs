a, b, c = map(int, input().split())

def f(n):
    if n == 0:
        return n

    r = n % 10

    return f(n // 10) + r

print(f(a * b * c))