n, k = map(int, input().split())
_list = list(map(int, input().split()))

_list = sorted(_list)
print(_list[k-1])