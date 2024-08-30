n = int(input())

x, y = 0, 0
dx, dy = [-1, 0, 0, 1], [0, -1, 1, 0]   # W, S, N, E

for _ in range(n):
    v, d = input().split()
    d = int(d)

    if v == "W":
        x = x + dx[0] * d
        y = y + dy[0] * d
    elif v == "S":
        x = x + dx[1] * d
        y = y + dy[1] * d
    elif v == "N":
        x = x + dx[2] * d
        y = y + dy[2] * d
    elif v == "E":
        x = x + dx[3] * d
        y = y + dy[3] * d

print(x, y)