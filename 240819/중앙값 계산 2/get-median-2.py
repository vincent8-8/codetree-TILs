n = int(input())
_list = list(map(int, input().split()))

for i in range(0, n):
    if i % 2 == 0: 
        t_list = _list[0 : i + 1]
        t_list.sort()

        print(t_list[i // 2], end=" ")