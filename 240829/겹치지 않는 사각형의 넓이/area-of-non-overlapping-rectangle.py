MAX_R = 2001

a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
m_x1, m_y1, m_x2, m_y2 = map(int, input().split())

graph = [ [0] * MAX_R for _ in range(MAX_R)]

for i in range(a_x1 + (MAX_R // 2), a_x2 + (MAX_R // 2)):
    for j in range(a_y1 + MAX_R // 2, a_y2 + MAX_R // 2):
        graph[i][j] = 1

for i in range(b_x1 + (MAX_R // 2), b_x2 + (MAX_R // 2)):
    for j in range(b_y1 + (MAX_R // 2), b_y2 + (MAX_R // 2)):
        graph[i][j] = 1

for i in range(m_x1 + (MAX_R // 2), m_x2 + (MAX_R // 2)):
    for j in range(m_y1 + (MAX_R // 2), m_y2 + (MAX_R // 2)):
        graph[i][j] = 0

cnt = 0
for i in range(0, MAX_R):
    for j in range(0, MAX_R):
        if graph[i][j] == 1:
            cnt += 1

print(cnt)