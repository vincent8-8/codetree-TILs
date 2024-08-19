n = int(input())
_list = list(map(int, input().split()))

_list = sorted(_list)
_list_reverse = _list[::-1]
min_max = 0

for i in range(n // 2 + 1):
    _sum = _list[i] + _list_reverse[i]
    if min_max < _sum:
        min_max = _sum
print(min_max)