n, b = map(int, input().split())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_cnt = 0

for i in range(n):
    total_prices = []
    local_sum = 0
    cnt = 0
    
    _list[i][0] //= 2

    for j in range(n):
        total_prices.append(_list[j][0] + _list[j][1])

    total_prices.sort()

    for k in range(n):
        local_sum += total_prices[k]
        if local_sum >= b:
            break
        cnt += 1

    max_cnt = max(max_cnt, cnt)

    _list[i][0] *= 2

print(max_cnt)