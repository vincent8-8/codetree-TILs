n = int(input())
_list = list(map(int, input().split()))
cnt = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if not (_list[0] - 2 <= i <= _list[0] + 2) and not (_list[1] - 2 <= j <= _list[1] + 2) and not (_list[2] - 2 <= k <= _list[2] + 2):
                cnt += 1
print(n * n * n - cnt)