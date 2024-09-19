import sys

n = int(input())
_list = list(map(int, input().split()))

_list.sort()
min_diff = sys.maxsize

for i in range(n):
    local_diff = _list[i + n] - _list[i]
    min_diff = min(min_diff, local_diff)

print(min_diff)