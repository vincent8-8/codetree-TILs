n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
min_dis = 2002

for i in range(n):
    for j in range(n):
        if i == j:
            continue
        x_d = (_list[i][0] - _list[j][0]) ** 2
        y_d = (_list[i][1] - _list[j][1]) ** 2

        dt = x_d + y_d

        min_dis = min(min_dis, dt)
    
print(min_dis)