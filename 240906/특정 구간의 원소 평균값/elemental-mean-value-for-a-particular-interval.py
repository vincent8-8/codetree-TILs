n = int(input())
_list = list(map(int, input().split()))
cnt = 0

for i in range(n):
    for j in range(n - i):
        avg = 0
        for k in range(i, i + j + 1):
            avg += _list[k]
        avg = avg / (j + 1)
        if avg in _list[i: i + j + 1]:
            cnt += 1
print(cnt)