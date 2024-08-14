n = int(input())
_list = list(map(int, input().split()))

def my_func(arr):
    for i in range(n):
        arr[i] = abs(arr[i])

my_func(_list)

for elem in _list:
    print(elem, end=" ")