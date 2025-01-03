n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
for i in range(n - 1):
    minimum = i
    
    for j in range(i + 1, n):
        if arr[minimum] > arr[j]:
            minimum = j
    
    if minimum != i:
        tmp = arr[i]
        arr[i] = arr[minimum]
        arr[minimum] = tmp

for elem in arr:
    print(elem, end=" ")