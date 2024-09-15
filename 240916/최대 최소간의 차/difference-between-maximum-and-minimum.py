n, k = map(int, input().split())
_list = list(map(int, input().split()))
_list.sort()

avg = round(sum(_list) / n)
k_2 = round(k / 2)
cost = 0

for i in range(n // 2):
    while not (avg - k_2) <= _list[i] <= (avg + k_2):
        if (avg - k_2) > _list[i]:
            _list[i] += 1
            cost += 1
        else:
            _list[i] -= 1
            cost += 1

_list.sort()

for j in range(-1, -(n // 2 + 1), -1):
    while _list[j] - _list[0] > k:
        _list[j] -= 1
        cost += 1

if n == 1:
    print("0")
else:
    print(cost)