import sys

_list = list(map(int, input().split()))
min_diff = sys.maxsize

def calculate(x, y, z):
    sum_1 = _list[x] + _list[y] + _list[z]
    sum_2 = sum(_list) - sum_1
    return abs(sum_1 - sum_2)

for i in range(6):
    for j in range(i + 1, 6):
        for k in range(j + 1, 6):
            min_diff = min(min_diff, calculate(i, j, k))
print(min_diff)