n = int(input())

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

graph = [
    list(input())
    for _ in range(n)
]

k = int(input())

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]  # D L U R
dir_num = (k - 1) // n
x, y = 0, 0

if ((k - 1) // n) % 2 == 0:
    if k - 1 < n:
        x, y = 0, k - 1
    else:
        x, y = n - 1, (n - 1) - ((k - 1) % n)
else:
    if k - 1 < (n * 2):
        x, y = (k - n - 1), n - 1
    else:
        x, y = (n - 1) - ((k - 1) % n), 0

keep_going = True
cnt = 1

while keep_going:
    if graph[x][y] == "/":
        if dir_num == 1 or dir_num == 3:
            dir_num = (dir_num + 3) % 4
        else:
            dir_num = (dir_num + 1) % 4
    else:
        if dir_num == 0 or dir_num == 2:
            dir_num = (dir_num + 3) % 4
        else:
            dir_num = (dir_num + 1) % 4
    
    nx, ny = (x + dxs[dir_num]), (y + dys[dir_num])
    if in_range(nx, ny):
        cnt += 1
    else:
        cnt += 1
        keep_going = False
    
print(cnt)