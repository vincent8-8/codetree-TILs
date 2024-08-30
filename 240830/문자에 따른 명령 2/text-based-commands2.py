qs = input()

x, y = 0, 0
dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for q  in qs:
    if q == "L":
        dir_num = (dir_num + 3) % 4
    elif q == "R":
        dir_num = (dir_num + 1) % 4
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)