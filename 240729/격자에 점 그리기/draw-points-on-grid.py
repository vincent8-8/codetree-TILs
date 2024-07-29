n, m = map(int, input().split())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

for i in range(1, m+1):
    p, q = map(int, input().split())
    arr[p-1][q-1] = i

for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()