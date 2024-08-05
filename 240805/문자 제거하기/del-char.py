s = input()

arr = list(s)
n = len(s) - 1

if n == 0:
    print(s)
else:
    for _ in range(n):
        index = int(input())

        if index < len(arr):
            arr.pop(index)
            print("".join(arr))
        else:
            arr.pop(-1)
            print("".join(arr))