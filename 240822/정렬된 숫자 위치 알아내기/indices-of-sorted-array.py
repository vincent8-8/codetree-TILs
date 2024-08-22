n = int(input())
_list = list(map(int, input().split()))
t_list = []
result = []

for i in range(n):
    v, befor_idx = _list[i], i
    t_list.append((v, befor_idx))

t_list.sort(key=lambda x: (x[0], x[1]) )

for i in range(n):
    v, befor_idx = t_list[i]
    after_idx = i
    result.append((v, befor_idx, after_idx))

result.sort(key=lambda x: x[1])

for _, _, idx in result:
    print(idx + 1, end=" ")