_list = list(map(int, input().split()))
_list.sort()
a, b = _list[0], _list[1]
c = 0

if (a + b) not in _list:
    c = _list[2]
else:
    c = _list[3]

print(a, b, c)