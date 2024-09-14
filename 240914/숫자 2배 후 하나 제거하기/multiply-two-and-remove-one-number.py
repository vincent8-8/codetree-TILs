import sys

n = int(input())
_list = list(map(int, input().split()))
min_sum = sys.maxsize

for i in range(n):
    _list[i] *= 2
    
    for j in range(n):
        local_sum = 0
        remaining_arr = [elem for k, elem in enumerate(_list) if k != j]

        for k in range(n - 2):
            local_sum += abs(remaining_arr[k + 1] - remaining_arr[k])

        min_sum = min(min_sum, local_sum)

    _list[i] //= 2

print(min_sum)