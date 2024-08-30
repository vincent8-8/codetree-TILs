n = int(input())
graph = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0] 
dir_num = 0
x, y = (n // 2), (n // 2)
graph[x][y] =1

i = 2

while i <= n * n:
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    if in_range(nx, ny) and graph[nx][ny] == 0:
        x, y = nx, ny
        graph[x][y] = i
        i += 1

    if in_range(nx + dxs[(dir_num + 1) % 4], ny + dys[(dir_num + 1) % 4] ) and graph[nx + dxs[(dir_num + 1) % 4]][ny + dys[(dir_num + 1) % 4]] == 0:
        dir_num = (dir_num + 1) % 4

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()