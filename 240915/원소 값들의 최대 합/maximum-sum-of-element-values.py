n, m = map(int, input().split())
_list = list(map(int, input().split()))

max_answer = 0

for i in range(n):
    local_sum = _list[i]
    start = _list[i]

    for _ in range(m - 1):
        local_sum += _list[start - 1]
        start = _list[start - 1]
    
    max_answer = max(max_answer, local_sum)

print(max_answer)