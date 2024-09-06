n, m = map(int, input().split())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
B_list.sort()
cnt = 0

for i in range(n - m + 1):
    tmp_list = A_list[i : i + m]

    if sorted(tmp_list) == B_list:
        cnt += 1

print(cnt)