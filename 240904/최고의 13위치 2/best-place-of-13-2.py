def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())
graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

history = []

for i in range(n):
    for j in range(n):
        if not in_range(i, j + 2):
            continue
        
        cnt = 0
        
        for k in range(0, 3):
            if graph[i][j + k] == 1:
                cnt += 1
        
        history.append(tuple((cnt, i, j)))

history.sort(key=lambda x: -x[0])

answer = history[0][0]

for coins, x, y in history:
    if (history[0][2] + 2) < y or (y + 2) < history[0][2] or x != history[0][1]:
        answer += coins
        break

print(answer)