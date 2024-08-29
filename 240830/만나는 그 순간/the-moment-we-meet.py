n, m = map(int, input().split())

pos_A = []
pos_B = []
 
for i in range(n):
    v, d = input().split()
    
    if v == "R":
        for j in range(int(d)):
            if not pos_A:
                pos_A.append(1)
            else:
                pos_A.append(pos_A[-1] + 1)
    elif v == "L":
        for j in range(int(d)):
            if not pos_A:
                pos_A.append(-1)
            else:
                pos_A.append(pos_A[-1] - 1)

for i in range(m):
    v, d = input().split()
    
    if v == "R":
        for j in range(int(d)):
            if not pos_B:
                pos_B.append(1)
            else:
                pos_B.append(pos_B[-1] + 1)
    elif v == "L":
        for j in range(int(d)):
            if not pos_B:
                pos_B.append(-1)
            else:
                pos_B.append(pos_B[-1] - 1)

# print(pos_A, pos_B) # check

cnt = -1

while pos_A:
    cnt += 1
    if pos_A.pop(0) == pos_B.pop(0):
        cnt += 1
        print(cnt)
        break
print("-1")