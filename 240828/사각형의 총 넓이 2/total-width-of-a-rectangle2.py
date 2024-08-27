n = int(input())

_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

_2d = [ [0] * 201 for _ in range(201)]

for elem in _list:
    for i in range(elem[0] + 100, elem[2] + 100):
        for j in range(elem[1] + 100, elem[3] + 100):
            _2d[j][i] = 1


cnt = 0
for elem in _2d:
    cnt += elem.count(1)

print(cnt)