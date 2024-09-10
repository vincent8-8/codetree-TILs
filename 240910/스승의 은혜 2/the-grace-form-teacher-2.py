n, b = map(int, input().split())
_list = [
    int(input())
    for _ in range(n)
]

max_num = 0
local_sum = 0

for i in range(n):
    _list[i] //= 2
    _list.sort()
    cnt = 0
    for j in range(n):
        local_sum += _list[j]

        if local_sum <= b:
            cnt += 1
        else:
            break
    
    _list[i] *= 2
    max_num = max(max_num, cnt)

print(max_num)