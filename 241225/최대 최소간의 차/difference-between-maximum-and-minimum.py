import sys

n, k = map(int, input().split())
_list = list(map(int, input().split()))
min_cost = sys.maxsize

for i in range(1, 10001 - k):
    cost = 0

    for elem in _list:
        if elem > i + k:
            cost += elem - (i + k)
        elif elem < i:
            cost += i - elem
        
    min_cost = min(min_cost, cost)

print(min_cost)