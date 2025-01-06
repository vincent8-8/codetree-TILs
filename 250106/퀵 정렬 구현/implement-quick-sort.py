n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
def quick_sort(arr, low, high):
    if low < high:
        pivot = high

        pivot_idx = partition(arr, low, high, pivot)

        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)


def partition(arr, low, high, pivot):   
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= arr[pivot]:
            i += 1
            swap(i, j)
    
    swap(i + 1, pivot)
    return i + 1

def swap(a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


def selec_pivot(low, high):
    if high - low >= 4:
        mid = (low + high) // 2
        candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
        _, idx = sorted(candidates, key = lambda x: x[0])[1]
        return idx
    else:
        return high

quick_sort(arr, 0, n - 1)

for elem in arr:
    print(elem, end=" ")
