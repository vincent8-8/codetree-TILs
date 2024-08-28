MAX_R = 201
OFFSET = 100

n = int(input())

_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

graph = [ [0] * MAX_R for _ in range(MAX_R)]

for x, y in _list:
    for i in range(x + OFFSET, x + 8 + OFFSET):
        for j in range(y + OFFSET, y + 8 + OFFSET):
            graph[i][j] = 1
        
cnt = 0

for i in range(0, MAX_R):
    for j in range(0, MAX_R):
        if graph[i][j] == 1:
            cnt += 1
print(cnt)