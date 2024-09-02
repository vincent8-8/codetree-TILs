n = int(input())
_list = list(map(int, input().split()))

max_sum = 0

for i in range(n):
    for j in range(i + 2, n):
        _sum = _list[i] + _list[j]
        if  _sum > max_sum:
            max_sum = _sum
print(max_sum)