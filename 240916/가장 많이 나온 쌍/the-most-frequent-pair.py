n, m = map(int, input().split())
_list = [
    list(map(int, input().split()))
    for _ in range(m)
]
max_cnt = 0

for i in range(m):
    cnt = 0
    for j in range(m):
        if i == j:
            continue
        if sorted(_list[i]) == sorted(_list[j]):
            cnt += 1
        
    max_cnt = max(max_cnt, cnt)

print(max_cnt + 1)