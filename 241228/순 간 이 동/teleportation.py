a, b, x, y = map(int, input().split())

distance = abs(a - b)
using_x = 0
using_y = 0

dist_a_x = abs(a - x)
dist_a_y = abs(a - y)

dist_b_x = abs(b - x)
dist_b_y = abs(b - y)


using_x += dist_a_x + dist_b_y
using_y = dist_a_y + dist_b_x

print(min(distance, using_x, using_y))
    