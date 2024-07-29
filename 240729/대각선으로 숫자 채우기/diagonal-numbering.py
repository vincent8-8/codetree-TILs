n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

cnt = 1

for i in range(n):
    if i == 0:
        for j in range(m):
            row = i
            while j >= 0 and row <= n-1:
                arr[row][j] = cnt
                cnt += 1
                row += 1
                j -= 1
    
    else:
        j = m-1
        row = i
        while j >= 0 and row <= n-1:
            arr[row][j] = cnt
            cnt += 1
            row += 1
            j -= 1

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()