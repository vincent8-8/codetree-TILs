n, m = map(int, input().split())
A_list = []
B_list = []

for _ in range(n):
    t, d = input().split()
    t = int(t)

    if not A_list:
        if d == "R":
            A_list.append(1)
            for _ in range(t - 1):
                A_list.append(A_list[-1] + 1)
        else:
            A_list.append(-1)
            for _ in range(t - 1):
                A_list.append(A_list[-1] - 1)
    else:
        if d == "R":
            for _ in range(t):
                A_list.append(A_list[-1] + 1)
        else:
            for _ in range(t):
                A_list.append(A_list[-1] - 1)

for _ in range(m):
    t, d = input().split()
    t = int(t)

    if not B_list:
        if d == "R":
            B_list.append(1)
            for _ in range(t - 1):
                B_list.append(B_list[-1] + 1)
        else:
            B_list.append(-1)
            for _ in range(t - 1):
                B_list.append(B_list[-1] - 1)
    else:
        if d == "R":
            for _ in range(t):
                B_list.append(B_list[-1] + 1)
        else:
            for _ in range(t):
                B_list.append(B_list[-1] - 1)

# init with random number
prev_A = A_list[0]
prev_B = B_list[0]

curr_A = 0
curr_B = 0

cnt = 0

while A_list or B_list:
    if A_list:
        curr_A = A_list.pop(0)

    if B_list:
        curr_B = B_list.pop(0)
    
    if curr_A == curr_B:
        if prev_A != prev_B:
            cnt += 1
            
    prev_A = curr_A
    prev_B = curr_B

print(cnt)