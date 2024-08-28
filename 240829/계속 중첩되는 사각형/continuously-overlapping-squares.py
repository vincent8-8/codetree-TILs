MAX_R = 201
OFFSET = 100

n = int(input())
_list = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
graph = [ [0] * MAX_R for _ in range(MAX_R) ]

for idx, (x1, y1, x2, y2) in enumerate(_list, start = 1):
    if idx % 2 == 1:
        color = 1 # means red
    else:
        color = 2 # means blue

    for i in range(x1 + OFFSET, x2 + OFFSET):
        for j in range(y1 + OFFSET, y2 + OFFSET):
            graph[i][j] = color
    
cnt = 0
for i in range(0, MAX_R):
    for j in range(0, MAX_R):
        if graph[i][j] == 2:
            cnt += 1
print(cnt)