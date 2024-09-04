n, m = map(int, input().split())
graph = [
    input()
    for _ in range(n)
]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# search every direction 
dxs, dys = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
cnt = 0

for i in range(n):
    for j in range(m):

        if graph[i][j] != "L":
            continue
        
        curx, cury = i, j

        for dx, dy in zip(dxs, dys):
            nx, ny = curx, cury
            find_answer = True

            for _ in range(2):
                nx, ny = nx + dx, ny + dy
                if not in_range(nx, ny) or graph[nx][ny] != "E":
                    find_answer = False                    
            
            if find_answer:
                cnt += 1

print(cnt)