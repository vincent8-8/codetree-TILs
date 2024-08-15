n = int(input())

def _recursive(n):
    if n == 0:
        return 

    print(n, end=" ")
    _recursive(n-1)
    print(n, end=" ")

_recursive(n)