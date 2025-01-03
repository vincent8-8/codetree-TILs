n = int(input())
arr = list(input().split())

# Write your code here!
for i in range(1, 7):
    digit_arr = [[] for _ in range(10)]
    
    for j in range(n):
        if len(arr[j]) < i:
            digit_arr[0].append(arr[j])
        else:
            digit_arr[int(arr[j][-i])].append(arr[j])
    
    save_arr = []

    for row in digit_arr:
        if row:
            for elem in row:
                save_arr.append(elem)
    
    arr = save_arr

for elem in arr:
    print(elem, end=" ")