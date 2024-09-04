n, k = map(int, input().split())
_list = list(map(int, input().split()))

max_sum = 0

for i in range(n - k + 1):
    local_sum = 0
    for j in range(i, i + k):
        local_sum += _list[j]
    max_sum = max(max_sum, local_sum)

print(max_sum)