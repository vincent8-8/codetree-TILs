n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
sorted_arr = [0] * n

def merge_sort(arr, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
    
def merge(arr, low, mid, high):
    i = low
    j = mid + 1
    k = low

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            sorted_arr[k] = arr[i]
            k+=1
            i+=1
        else:
            sorted_arr[k] = arr[j]
            k+=1
            j+=1
    
    while i <= mid:
        sorted_arr[k] = arr[i]
        i+=1
        k+=1

    while j <= high:
        sorted_arr[k] = arr[j]
        j+=1
        k+=1

    for k in range(low, high + 1):
        arr[k] = sorted_arr[k]
    

merge_sort(arr, 0, len(arr) - 1)

for elem in arr:
    print(elem, end=" ")