n = int(input())
_list = [
    list(input().split())
    for _ in range(n)
]

d_arr = []

for elem in _list:

    if len(elem) == 1:
        if elem[0] == "pop_back":
            d_arr.pop(-1)
        elif elem[0] == "size":
            print(len(d_arr))
    else:
        if elem[0] == "push_back":
            d_arr.append(int(elem[1]))
        elif elem[0] == "get":
            print(d_arr[int(elem[1]) - 1])