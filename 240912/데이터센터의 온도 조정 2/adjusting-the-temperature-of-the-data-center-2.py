n, c, g, h = map(int, input().split())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_sum = 0

for i in range(0, 1001):
    local_sum = 0

    for ta, tb in _list:
        if i < ta:
            local_sum += c
        elif ta <= i <= tb:
            local_sum += g
        else:
            local_sum += h
    
    max_sum = max(max_sum, local_sum)
print(max_sum)