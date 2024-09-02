n = int(input())
_list = [
    int(input())
    for _ in range(n)
]

total = []

for i in range(n):
    local_total = 0
    for j in range(n):
        if i == j:
            continue
        else:
            if (j - i) > 0:
                local_total += _list[j] * (j - i)
            else:
                local_total += _list[j] * (j - i + n)
                
    total.append(local_total)

print(min(total))