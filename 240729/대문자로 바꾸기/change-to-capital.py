list_2d = [
    list(input().split())
    for _ in range(5)
]

for i in range(5):
    for j in range(3):
        print(list_2d[i][j].upper(), end=" ")
    print()