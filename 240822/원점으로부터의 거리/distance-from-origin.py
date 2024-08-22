n = int(input())
_list = []

for i in range(n):
    x, y = map(int, input().split())
    _list.append((x, y, i+1))

_list.sort(key=lambda x: ( ( abs(int(x[0])) + abs(int(x[1])) ), x[2] ))

for _, _, idx in _list:
    print(idx)