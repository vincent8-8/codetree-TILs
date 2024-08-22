n = int(input())
_list = []

for i in range(n):
    h, w = map(int, input().split())
    _list.append(tuple((h, w, i+1)))

_list.sort(key=lambda x: (-x[0], -x[1], x[2]))

for h, w, n in _list:
    print(h, w, n)