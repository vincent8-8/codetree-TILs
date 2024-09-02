r, c = map(int, input().split())
_list = [
    list(input().split())
    for _ in range(r)
]

start_color = _list[0][0]
cnt = 0

for i in range(1, r):
    for j in range(1, c):
        for k in range(i + 1, r):
            for l in range(j + 1, c):
                if _list[i][j] != start_color and _list[k][l] == start_color:
                    if k != (r - 1) and l != (c - 1):
                        cnt += 1
if _list[0][0] == _list[r - 1][c - 1]:
    print("0")
else:
    print(cnt)