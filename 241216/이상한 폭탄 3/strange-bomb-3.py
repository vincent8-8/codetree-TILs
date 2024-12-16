n, k = map(int, input().split())
_list = [int(input()) for _ in range(n)]
max_count = 0

for i, elem in enumerate(_list):
    count = 0

    for j in range(i + 1, n):
        if _list[j] == elem:
            if j - i <= k:
                count += 1
    
    max_count = max(max_count, count)

print(max_count)