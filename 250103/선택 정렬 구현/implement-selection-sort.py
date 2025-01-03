n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
for i in range(n - 1):
    min_val = min(arr[i + 1: n])
    idx = arr.index(min_val)
    
    if arr[i] > arr[idx]:
        tmp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = tmp

for elem in arr:
    print(elem, end=" ")