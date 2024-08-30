n, t = map(int, input().split())
g = [[0] * (n + 1) for _ in range(n + 1)]
r, c, d = input().split()

def in_range(x, y):
    return 1 <= x and x < n + 1 and 1 <= y and y < n + 1

dxs, dys = [0, -1, 1, 0], [-1, 0, 0, 1]
mapper = {
    "L" : 0,
    "D" : 1,
    "U" : 2,
    "R" : 3
}

dir_num = mapper[d]
x, y = int(r), int(c)

for _ in range(t):
    nx, ny = (x + dxs[dir_num]), (y + dys[dir_num])
    if in_range(nx, ny):
        x, y = nx, ny
    else:
        dir_num = (3 - dir_num) % 4

print(x, y)