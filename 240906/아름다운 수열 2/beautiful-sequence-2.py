n, m = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
cnt = 0

for i in range(n - m + 1):
    is_ans = True
    tmp_list = A_list[i : i + m]

    for j in range(m):
        if not B_list[j] in tmp_list:
            is_ans = False
            break
    
    if is_ans:
        cnt += 1

print(cnt)