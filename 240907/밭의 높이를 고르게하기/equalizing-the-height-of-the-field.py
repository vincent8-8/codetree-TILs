import sys

n, h, t = map(int, input().split())
_list = list(map(int, input().split()))
min_cost = sys.maxsize

for i in range(n - t + 1):
    cost = 0
    for j in range(i, i + t):
        cost += abs(_list[j] - h)
    
    if cost < min_cost:
        min_cost = cost
print(min_cost)