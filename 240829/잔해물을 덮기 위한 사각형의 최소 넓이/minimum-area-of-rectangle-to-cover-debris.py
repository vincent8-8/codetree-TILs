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

max_distance_x = 0
max_distance_y = 0

for i in range(0, MAX_R):
    distance_x = 0
    distance_y = 0
    x1, x2, y1, y2 = -1, -1, -1, -1

    for j in range(0, MAX_R):

        if x1 == -1:
            if graph[i][j] == 1:
                x1 = j
        
        if y1 == -1:
            if graph[j][i] == 1:
                y1 = j

        if graph[i][j] == 1:
            x2 = j
        
        if graph[j][i] == 1:
            y2 = j

    distance_x = x2 - x1 + 1
    distance_y = y2 - y1 + 1

    if max_distance_x < distance_x:
        max_distance_x = distance_x
    if max_distance_y < distance_y:
        max_distance_y = distance_y
    
print(max_distance_x * max_distance_y)