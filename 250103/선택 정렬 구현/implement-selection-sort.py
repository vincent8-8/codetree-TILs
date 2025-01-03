n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
for i in range(n):
    min_val = min(arr[i: n])
    idx = arr.index(min_val)
    
    if arr[i] > arr[idx]:
        tmp = arr[i]
        arr[i] = arr[idx]
        arr[idx] = tmp

for elem in arr:
    print(elem, end=" ")