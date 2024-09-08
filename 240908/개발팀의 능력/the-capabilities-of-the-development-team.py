import sys

_list = list(map(int, input().split()))
min_diff = sys.maxsize

def calc(x, y, q, w):
    sum3 = sum(_list)
    sum1 = _list[x] + _list[y]
    sum2 = _list[q] + _list[w]
    sum3 = sum3 - sum1 - sum2

    if sum1 != sum2 and sum1 != sum3 and sum2 != sum3:
        return abs(max(sum1, sum2, sum3) - min(sum1, sum2, sum3))
    else:
        return sys.maxsize

for i in range(5):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                if i == j or i == k or i == l or j == k or j == l or k == l:
                    continue
                local_diff = calc(i, j, k, l)

                if local_diff < min_diff:
                    min_diff = local_diff
if min_diff < 5000:
    print(min_diff)
else:
    print("-1")