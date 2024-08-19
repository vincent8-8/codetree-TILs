n = int(input())
_list = list(map(int, input().split()))

for i in range(1, n + 1):
    if i % 2 == 1: 
        print(_list[i // 2], end=" ")