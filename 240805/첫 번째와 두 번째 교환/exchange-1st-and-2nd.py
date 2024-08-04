s = input()

arr = list(s)

first = arr[0]
second = arr[1]

for i in range(0, len(arr)):
    if arr[i] == first:
        arr[i] = second
    elif arr[i] == second:
        arr[i] = first


for elem in arr:
    print(elem, end="")