n, k = map(int, input().split())
_list = list(map(int, input().split()))

avg = round(sum(_list) / n)
cost = 0

for i in range(n):
    for j in range(i + 1, n):
        if abs(_list[i] - _list[j]) <= k:
            continue
        
        while abs(_list[i] - _list[j]) > k:
            if abs(_list[i] - avg) > abs(_list[j] - avg):
                if _list[i] - avg > 0:
                    _list[i] -= 1
                else:
                    _list[i] += 1
                
            else:
                if _list[j] - avg > 0:
                    _list[j] -= 1
                else:
                    _list[j] += 1
                
            cost += 1

print(cost)