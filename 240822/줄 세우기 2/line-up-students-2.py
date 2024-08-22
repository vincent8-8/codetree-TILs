n = int(input())
_list = []

for i in range(n):
    h, w = map(int, input().split())
    _list.append((h, w, i))

_list.sort(key=lambda x: ( x[0], -x[1] ) )

for h, w, i in _list:
    print(h, w, i+1)