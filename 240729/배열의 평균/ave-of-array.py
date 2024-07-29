list_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    print(round(sum(list_2d[i])/4, 1), end=" ")

print()

for j in range(4):
    print(round((list_2d[0][j] + list_2d[1][j])/2, 1), end=" ")

print()

print(round((sum(list_2d[0]) + sum(list_2d[1])) / 8, 1))