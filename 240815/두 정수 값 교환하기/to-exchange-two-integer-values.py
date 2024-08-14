a, b = map(int, input().split())

def change(a, b):
    return b, a

a, b = change(a, b)
print(a, b)