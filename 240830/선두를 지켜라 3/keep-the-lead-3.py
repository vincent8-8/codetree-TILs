n, m = map(int, input().split())

head = ""

pos_A = []
pos_B = []

for _ in range(n):
    v, t = map(int, input().split())
    if not pos_A:
        pos_A.append(v)
        for _ in range(t - 1):
            pos_A.append(pos_A[-1] + v)
    else:
        for _ in range(t):
            pos_A.append(pos_A[-1] + v)

for _ in range(m):
    v, t = map(int, input().split())
    if not pos_B:
        pos_B.append(v)
        for _ in range(t - 1):
            pos_B.append(pos_B[-1] + v)
    else:
        for _ in range(t):
            pos_B.append(pos_B[-1] + v)

cnt = 0

for i in range(len(pos_A)):
    if pos_A[i] > pos_B[i]:
        if head != "A":
            cnt += 1
        head = "A"
    elif pos_A[i] < pos_B[i]:
        if head != "B":
            cnt += 1
        head = "B"
    else:
        if head != "=":
            cnt += 1
        head = "="

print(cnt)