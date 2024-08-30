OFFSET = 65
n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] 
dir_num = 0
graph[0][0] = 'A'
x, y = 0, 0

i = 1

while i < n * m:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if in_range(nx, ny) and graph[nx][ny] == 0:
        x, y = nx, ny
        graph[x][y] = chr((i % 26) + OFFSET)
        i += 1
    else:
        dir_num = (dir_num + 1) % 4

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=" ")
    print()