MAX_R = 2001
OFFSET = 1000

n = int(input())
graph = [[0] * MAX_R for _ in range(MAX_R)]
x, y = OFFSET, OFFSET

dxs, dys = [0, -1, 1, 0], [-1, 0, 0, 1]
mapper = {
    'E' : 0,
    'S' : 1,
    'N' : 2,
    'W' : 3
}
t = 0
find_answer = False

for _ in range(n):
    v, d = input().split()
    dir_num = mapper[v]

    for _ in range(int(d)):
        x, y = (x + dxs[dir_num]), (y + dys[dir_num])
        t += 1
        
        if x == OFFSET and y == OFFSET:
            print(t)
            find_answer = True
            break
    
    if find_answer:
        break
        
if not find_answer:
    print("-1")