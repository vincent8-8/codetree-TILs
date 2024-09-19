_list = list(map(int, input().split()))
_list.sort()
a, b = _list[0], _list[1]
c, d = 0, 0

if (a + b) != _list[2]:
    c = _list[2]
    _list.remove(a + b)
    _list.remove(a + c)
    _list.remove(b + c)

    d = _list[3]
else:
    c = _list[3]
    _list.remove(a + b)
    _list.remove(a + c)
    _list.remove(b + c)

    d = _list[4]

print(a, b, c, d)