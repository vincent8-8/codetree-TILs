n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_sum = 0

for i in range(n):
    for j in range(n - 2):
        max_sum = max(max_sum, _list[i][j] + _list[i][j + 1] + _list[i][j + 2])
print(max_sum)