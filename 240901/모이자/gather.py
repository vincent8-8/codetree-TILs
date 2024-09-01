import sys

MIN_SUM = sys.maxsize

n = int(input())
_list = list(map(int, input().split()))

for i in range(n):
    local_sum = 0
    for j in range(n):
        local_sum += _list[j] * abs(j - i)

    if local_sum < MIN_SUM:
        MIN_SUM = local_sum
print(MIN_SUM)