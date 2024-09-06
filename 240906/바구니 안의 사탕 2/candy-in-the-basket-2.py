n, k = map(int, input().split())
_list = [0] * 100
max_cnt = 0

for _ in range(n):
    candies, idx = map(int, input().split())
    _list[idx - 1] = candies
 
for i in range(k, 100 - k):
    cnt = 0
    for j in range(i - k, i + k + 1):
        if _list[j] == 0:
            continue
        
        cnt += _list[j]
    max_cnt = max(max_cnt, cnt)

print(max_cnt)