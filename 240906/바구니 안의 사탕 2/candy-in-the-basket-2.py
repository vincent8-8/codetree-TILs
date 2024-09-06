n, k = map(int, input().split())
_list = [0] * 101
max_cnt = 0

for _ in range(n):
    candies, idx = map(int, input().split())
    _list[idx] = candies
 
for i in range(0, 101):
    cnt = 0
    if k * 2 > 101:
        cnt = sum(_list)

    elif i - k < 0:
        for j in range(0, i + k + 1):
            if _list[j] == 0:
                continue
            cnt += _list[j]

    elif i + k >= 100:
        for j in range(i - k, 101):
            if _list[j] == 0:
                continue
            cnt += _list[j]

    else:
        for j in range(i - k, i + k + 1):
            if _list[j] == 0:
                continue
            cnt += _list[j]

    max_cnt = max(max_cnt, cnt)

print(max_cnt)