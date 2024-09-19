_list = [
    list(map(int, input().split()))
    for _ in range(2)
]

a1, a2, b1, b2 = _list[0]
c1, c2, d1, d2 = _list[1]

w = max(a1, b1, c1, d1) - min(a1, b1, c1, d1)
h = max(a2, b2, c2, d2) - min(a2, b2, c2, d2)

print(w * h)