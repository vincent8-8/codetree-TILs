n, m = map(int, input().split())

arr_2d = [
    [0 for _ in range(m)]
    for _ in range(n)
]

count = 1

for row in arr_2d:
    for elem in row:
        elem = count
        print(elem, end=" ")
        count += 1
    print()