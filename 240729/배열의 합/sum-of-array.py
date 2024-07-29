list_2d = [
    list(map(int, input().split()))
    for _ in range(4)
]

for i in range(0, len(list_2d)):
    print(sum(list_2d[i]))