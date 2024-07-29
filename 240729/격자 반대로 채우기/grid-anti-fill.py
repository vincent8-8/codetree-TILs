n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1

for i in range(n-1, -1, -2):
    for j in range(n-1, -1, -1):
        arr[j][i] = cnt
        cnt += 1
    cnt += n

cnt = n + 1

for i in range(n-2, -1, -2):
    for j in range(n):
        arr[j][i] = cnt
        cnt += 1
    cnt += n

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()