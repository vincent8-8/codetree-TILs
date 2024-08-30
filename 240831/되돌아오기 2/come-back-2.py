MAX_R = 200001
OFFSET = 100000

qs = input()
time = 0

dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]
x, y = OFFSET, OFFSET
dir_num = 2
returned = False

for q in qs:
    if q == "F":
        x, y = (x + dxs[dir_num]), (y + dys[dir_num])
    elif q == "R":
        dir_num = (dir_num + 1) % 4
    else:
        dir_num = (dir_num + 3) % 4
    
    time += 1
    if x == OFFSET and y == OFFSET:
        print(time)
        returned = True

if not returned:
    print("-1")