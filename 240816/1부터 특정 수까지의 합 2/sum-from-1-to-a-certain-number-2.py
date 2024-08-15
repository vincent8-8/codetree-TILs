n = int(input())

def _recursive(n):
    if n == 1:
        return 1
    return _recursive(n-1) + n

print(_recursive(n))