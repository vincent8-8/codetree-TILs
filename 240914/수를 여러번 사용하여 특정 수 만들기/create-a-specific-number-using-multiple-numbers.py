MAX_NUM = 1000
a, b, c = map(int, input().split())

max_sum = 0

for i in range(MAX_NUM):
    for j in range(MAX_NUM):
        local_sum = (a * i) + (b * j)
        if local_sum <= c:
            max_sum = max(max_sum, local_sum)

print(max_sum)