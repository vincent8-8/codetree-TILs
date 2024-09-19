_list = list(map(int, input().split()))
_list.sort()
a, b = _list[0], _list[1]
c = 0

if (a + b) == _list[2]:
    c = _list[3]
else:
    c = _list[2]

print(a, b, c)