n = int(input())
_list = list(map(int, input().split()))

def new_list(arr):
    for i in range(0, n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2



new_list(_list)
for elem in _list:
    print(elem, end=" ")