_list = list(map(int, input().split()))

cost = 0

while True:
    diff_a_b = _list[1] - _list[0]
    diff_b_c = _list[2] - _list[1]

    if diff_a_b == 1 and diff_b_c == 1:
        break

    if diff_a_b < diff_b_c:
        cost += 1

        if diff_a_b == 1:
            if (_list[1] + _list[2]) % 2 == 0:
                _list[0] = (_list[1] + _list[2]) // 2
            else:
                _list[0] = (_list[1] + _list[2]) // 2 + 1
        else:
            if (_list[0] + _list[1]) % 2 == 0:
                _list[2] = (_list[0] + _list[1]) // 2
            else:
                _list[2] = (_list[0] + _list[1]) // 2 + 1
    else:
        cost += 1
        if diff_b_c == 1:
            if (_list[0] + _list[1]) % 2 == 0:
                _list[2] = (_list[0] + _list[1]) // 2
            else:
                _list[2] = (_list[0] + _list[1]) // 2 + 1
        else:
            if (_list[1] + _list[2]) % 2 == 0:
                _list[0] = (_list[1] + _list[2]) // 2
            else:
                _list[0] = (_list[1] + _list[2]) // 2 + 1

    _list.sort()

print(cost)