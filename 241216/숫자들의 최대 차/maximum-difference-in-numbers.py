n, k = map(int, input().split())
_list = [int(input()) for _ in range(n)]
max_count = -1

for selec in _list:
    count = 0

    for elem in _list:
        if selec <= elem and elem <= (selec + k):
            count += 1
        else:
            continue
    
    max_count = max(max_count, count)

print(max_count)