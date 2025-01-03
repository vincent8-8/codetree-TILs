n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

for i in range(n - 1):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            tmp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = tmp

for elem in arr:
    print(elem, end=" ")