_pos = list(map(int, input().split()))
_pos.sort()

dist_a_b = _pos[1] - _pos[0]
dist_b_c = _pos[2] - _pos[1]

cost = 0

if dist_a_b == 1 and dist_b_c == 1:
    pass
elif dist_a_b > dist_b_c:
    cost = dist_a_b - 1
else:
    cost = dist_b_c - 1

print(cost)