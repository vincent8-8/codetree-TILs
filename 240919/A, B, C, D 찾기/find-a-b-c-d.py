_list = list(map(int, input().split()))
_list.sort()
a, b = _list[0], _list[1]
c, d = 0, 0

if (a + b) != _list[2]:
    c = _list[2]
else:
    c = _list[3]

d = _list[-1] - c - b - a

print(a, b, c, d)