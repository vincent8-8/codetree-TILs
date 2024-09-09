n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
work_time = [ [0] for _ in range(1000)]

max_time = 0
local_sum = 0

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        start, end = _list[j]

        for k in range(start, end):
            work_time[k] = 1
        
    local_sum = work_time.count(1)
    max_time = max(max_time, local_sum)
    
    for l in range(1000):
        work_time[l] = 0
print(max_time)