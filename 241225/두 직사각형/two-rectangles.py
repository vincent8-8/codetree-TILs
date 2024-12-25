a1, a2, b1, b2 = map(int, input().split())
c1, c2, d1, d2 = map(int, input().split())

if b1 < c1 or d1 < a1:
    print("nonoverlapping")
elif b2 < c2 or d2 < a2:
    print("nonoverlapping")
else:
    print("overlapping")