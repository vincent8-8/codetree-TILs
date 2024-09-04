import sys

n, s = map(int, input().split())
_list = list(map(int, input().split()))

min_diff = sys.maxsize

for i in range(n):
    for j in range(i + 1, n):
        diff = 0
        list_sum = 0

        list_sum = sum(_list[0:i]) + sum(_list[i + 1 : j]) + sum(_list[j + 1 :])
        diff = abs(s - list_sum)

        if min_diff > diff:
            min_diff = diff

print(min_diff)