_list = list(map(int, input().split()))
diff = max(_list) - min(_list)
cost = 0

if _list[1] - _list[0] < _list[2] - _list[1]:
    while not diff == 2:
        cost += 1
        _list.sort()
        _list[2] =  ((_list[0] + _list[1]) // 2) if (_list[0] + _list[1]) % 2 == 0 else ((_list[0] + _list[1]) // 2 + 1) 
        
        diff = max(_list) - min(_list)

else:
    while not diff == 2:
        cost += 1
        _list.sort()
        _list[0] =  ((_list[1] + _list[2]) // 2) if (_list[1] + _list[2]) % 2 == 0 else ((_list[1] + _list[2]) // 2 + 1) 

        diff = max(_list) - min(_list)

print(cost)