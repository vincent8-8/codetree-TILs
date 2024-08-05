s = input()

arr = list(s)
n = len(s) - 1

for _ in range(n):
    index = int(input())

    if index < n:
        arr.pop(index)
        print("".join(arr))
    else:
        arr.pop(-1)
        print("".join(arr))