_list = list(map(int, input().split()))
_list.sort()
diff_a_b = _list[1] - _list[0]
diff_b_c = _list[2] - _list[1]

if diff_a_b == 1 and diff_b_c == 1:
    print(0)
elif diff_a_b == 2 or diff_b_c == 2:
    print(1)
else:
    print(2)