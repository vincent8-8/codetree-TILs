n, b = map(int, input().split())
_list = [
    int(input())
    for _ in range(n)
]

_list.sort()
max_num = 0
local_sum = 0

for i in range(n):
    _list[i] //= 2
    cnt = 0
    for j in range(n):
        if local_sum + _list[j] >= b:
            break
        local_sum += _list[j]
        cnt += 1
    
    max_num = max(max_num, cnt)

print(max_num)