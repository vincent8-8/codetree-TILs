def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n, m = map(int, input().split())

graph = [ [0] * n for _ in range(m)]
graph[0][0] = 1

dxs, dys = [0, -1, 0, 1], [1, 0, -1, 0]
dir_num = 0
x, y = 0, 0
num = 2

while True:
    nx, ny = (x + dxs[dir_num]), (y + dys[dir_num])

    if in_range(nx, ny) and graph[nx][ny] == 0:
        graph[nx][ny] = num
        num += 1
        x, y = nx, ny
    else:
        dir_num = (dir_num + 1) % 4

    if num > n * m:
        break

for column in graph:
    for elem in column:
        print(elem, end = " ")
    print()