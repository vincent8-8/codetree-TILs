x, y = map(int, input().split())
max_sum = 0

for i in range(x, y + 1):
    to_str = str(i)
    local_sum = 0

    for elem in to_str:
        local_sum += int(elem)
    
    max_sum = max(max_sum, local_sum)

print(max_sum)