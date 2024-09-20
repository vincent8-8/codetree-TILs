n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_answer = 101

for i in range(n):
    min_x = 101
    max_x = 0

    for j in range(n):
        if i == j:
            continue

        x1, x2 = _list[j]
        
        min_x = min(min_x, x1)
        max_x = max(max_x, x2)

    answer = max_x - min_x

    min_answer = min(min_answer, answer)

print(min_answer)