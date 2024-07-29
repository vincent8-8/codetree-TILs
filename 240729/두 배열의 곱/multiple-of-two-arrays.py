arr1_2d = [
    list(map(int, input().split()))
    for _ in range(3)
]
input()
arr2_2d = [
    list(map(int, input().split(" ")))
    for _ in range(3)
]

for i in range(2):
    for j in range(2):
        print(arr1_2d[i][j])
        print(arr2_2d[i][j])
        print(arr1_2d[i][j] * arr2_2d[i][j], end = " ")

    print()