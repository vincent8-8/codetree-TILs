MAX_R = 2001
OFFSET = 1000

a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
graph = [ [0] * MAX_R for _ in range(MAX_R) ]

for i in range(a_x1 + OFFSET, a_x2 +OFFSET):
    for j in range(a_y1 + OFFSET, a_y2 + OFFSET):
        graph[i][j] = 1

for i in range(b_x1 + OFFSET, b_x2 +OFFSET):
    for j in range(b_y1 + OFFSET, b_y2 + OFFSET):
        graph[i][j] = 0

max_continued_x = 0
max_continued_y = 0

for i in range(0, MAX_R):
    continued_x = 0
    continued_y = 0

    for j in range(0, MAX_R):
        if graph[i][j] == 1:
            continued_x += 1
        
        if graph[j][i] == 1:
            continued_y += 1

    if max_continued_x < continued_x:
        max_continued_x = continued_x
    if max_continued_y < continued_y:
        max_continued_y = continued_y
    
print(max_continued_x * max_continued_y)