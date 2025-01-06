n = int(input())
arr = [0] + list(map(int, input().split()))

# Write your code here!
def heap_sort(n):
    for i in range(n // 2, 0, -1):
        heapify(n, i)
    
    for i in range(n, 0, -1):
        swap(1, i)
        heapify(i - 1, 1)

def heapify(n, i):
    maximum = i
    l = i * 2
    r = i * 2 + 1

    if l <= n and arr[maximum] < arr[i * 2]:
        maximum = l
    
    if r <= n and arr[maximum] < arr[i * 2 + 1]:
        maximum = r
    
    if maximum != i:
        swap(i, maximum)
        heapify(n, maximum)

def swap(a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

heap_sort(n)

for i in range(1, n + 1):
    print(arr[i], end=" ")