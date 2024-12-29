_list = list(map(int, input().split()))
diff = max(_list) - min(_list)
cost = 0

while not diff == 2:
    cost += 1
    _list.sort()
    _list[2] = (_list[0] + _list[1]) // 2

    diff = max(_list) - min(_list)

print(cost)