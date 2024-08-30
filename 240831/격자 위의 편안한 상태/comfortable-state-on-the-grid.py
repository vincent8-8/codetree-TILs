n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]

for _ in range(m):
    r, c = map(int, input().split())
    x, y = r - 1, c - 1
    graph[x][y] = 1
    cnt = 0

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and graph[nx][ny] == 1:
            cnt += 1
    if cnt == 3:
        print("1")
    else:
        print("0")