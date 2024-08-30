def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n, t = map(int, input().split())
qs = input()
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = n // 2, n // 2
dir_num = 0

_sum = graph[x][y]

for i in range(t):
    if qs[i] == 'F':
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if in_range(nx, ny):
            x, y = nx, ny
            _sum += graph[x][y]

    elif qs[i] == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        dir_num = (dir_num + 3) % 4

print(_sum)