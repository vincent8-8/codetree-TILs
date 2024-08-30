MAX_R = 2000001
OFFSET = 1000000

pos_A = [0] * MAX_R
pos_B = [0] * MAX_R
curr_A = OFFSET
curr_B = OFFSET

# relative postion (which one is left? A or B)
left = ""

n, m = map(int, input().split())

for i in range(1, n + 1):
    t, d = input().split()
    t = int(t)

    if d == "R":
        curr_A += t
        pos_A[curr_A] = i
    else:
        curr_A -= t
        pos_A[curr_A] = i

for i in range(1, m + 1):
    t, d = input().split()
    t = int(t)

    if d == "R":
        curr_B += t
        pos_B[curr_B] = i
    else:
        curr_B -= t
        pos_B[curr_B] = i

i, j = 1, 1
cnt = 0

while i != n or j != m:

    A = pos_A.index(i)
    B = pos_B.index(j)

    if A < B:
        if left == "B":
            cnt += 1
        left = "A"
    elif A > B:
        if left == "A":
            cnt += 1
        left = "B"

    if i < n:
        i += 1
    if j < m:
        j += 1

print(cnt)