n, k = map(int, input().split())
_list = list(map(int, input().split()))
_list.sort()
cost = 0
avg = sum(_list) / n

while True:
    if _list[-1] - _list[0] <= k:
        break

    l_count = 0
    r_count = 0
    avg = sum(_list) / n

    for i in range(n):
        if _list[i] < (avg - k / 2):
            l_count += 1
        elif _list[i] > (avg + k / 2):
            r_count += 1
    
    if l_count > r_count:
        _list[-1] -= 1
    else:
        _list[0] += 1
    
    cost += 1
    _list.sort()

print(cost)