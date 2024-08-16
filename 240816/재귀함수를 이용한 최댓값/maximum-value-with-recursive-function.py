n = int(input())
_list = list(map(int, input().split()))

def f(n):
    if n < 0:
        return _list[-1]

    if _list[-1] < _list[n]:
        _list[-1] = _list[n]
    return f(n - 1)

print(f(n-1))