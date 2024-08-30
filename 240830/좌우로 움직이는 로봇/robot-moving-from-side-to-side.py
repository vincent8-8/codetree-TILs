pos_A = []
pos_B = []
curr_A = 0
curr_B = 0

# relative postion (which one is left? A or B)
left = ""

n, m = map(int, input().split())

for i in range(0, n):
    t, d = input().split()
    t = int(t)

    if d == "R":
        curr_A += t
    else:
        curr_A -= t
    
    pos_A.append(curr_A)

for j in range(0, m):
    t, d = input().split()
    t = int(t)

    if d == "R":
        curr_B += t
    else:
        curr_B -= t
    
    pos_B.append(curr_B)

i = 0
j = 0
cnt = 0

while (i < n) or (j < m):
    A = pos_A[i]
    B = pos_B[j]

    if A < B:
        if left == "B":
            cnt += 1
        left = "A"
    elif A > B:
        if left == "A":
            cnt += 1
        left = "B"
    
    
    if i >= n - 1 and j >= m - 1:
        break

    if i + 1 < n:
        i += 1
    if j + 1 < m:
        j += 1


print(cnt)