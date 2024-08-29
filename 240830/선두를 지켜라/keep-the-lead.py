n, m = map(int, input().split())
pos_A = []
pos_B = []

for _ in range(n):
    v, t = map(int, input().split())
    
    if not pos_A:
        pos_A.append(v)
        for _ in range(t-1):
            pos_A.append(pos_A[-1] + v)
    else:
        for _ in range(t):
            pos_A.append(pos_A[-1] + v)

for _ in range(m):
    v, t = map(int, input().split())
    
    if not pos_B:
        pos_B.append(v)
        for _ in range(t-1):
            pos_B.append(pos_B[-1] + v)
    else:
        for _ in range(t):
            pos_B.append(pos_B[-1] + v)

changed = 0
front = ""

for A_pos, B_pos in zip(pos_A, pos_B):
    if A_pos > B_pos:
        if front == "B":
            changed += 1
            front = "A"
        else:
            front = "A"
    elif A_pos < B_pos:
        if front == "A":
            changed += 1
            front = "B"
        else:
            front = "B"

print(changed)