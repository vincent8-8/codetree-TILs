_list = [
    list(map(int, input().split()))
    for _ in range(2)
]

x1, y1, x2, y2 = _list[0]
x3, y3, x4, y4 = _list[1]

w = max(x2, x4) - min(x1, x3)
h= max(y2, y4) - min(y1, y3)
s = max(w, h)
print(s ** 2)