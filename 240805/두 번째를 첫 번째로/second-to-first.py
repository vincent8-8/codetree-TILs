s = input()

arr = list(s)
l = arr[1]

for i in range(1, len(arr)):
    if arr[i] == l:
        arr[i] = arr[0]

print("".join(arr))