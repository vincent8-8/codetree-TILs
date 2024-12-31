_graph = [input() for _ in range(10)]
l_b_cordinate = []

for row in range(10):
    for column in range(10):
        if _graph[row][column] == 'B':
            l_b_cordinate.append([row, column])
        elif _graph[row][column] == 'L':
            l_b_cordinate.append([row, column])

ver_dist = (abs(l_b_cordinate[0][0] - l_b_cordinate[1][0]) - 1) if abs(l_b_cordinate[0][0] - l_b_cordinate[1][0]) > 1 else 0
hor_dist = (abs(l_b_cordinate[0][1] - l_b_cordinate[1][1]) - 1) if abs(l_b_cordinate[0][1] - l_b_cordinate[1][1]) > 1 else 0

if ver_dist == 0 and hor_dist == 0:
    print(0)
elif ver_dist >= 1 and hor_dist >= 1:
    print(ver_dist + hor_dist + 1)
else:
    print(ver_dist + hor_dist)