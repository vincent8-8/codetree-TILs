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

length = len(history)
max_coins = 0

for i in range(length):
    for j in range(i + 1, length):
        coins = 0

        if ( (history[i][2] + 2) < (history[j][2]) ) or ( history[i][2] > history[j][2] + 2 ) or ( history[i][1] != history[j][1] ):
            coins = history[i][0] + history[j][0]
        
        if max_coins < coins:
            max_coins = coins

print(max_coins)