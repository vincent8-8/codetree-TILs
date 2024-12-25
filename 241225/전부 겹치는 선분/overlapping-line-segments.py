n = int(input())
_list = [list(map(int, input().split())) for _ in range(n)]

_graph = [0] * 101

for line in _list:
    for i in range(line[0], line[1] + 1):
        _graph[i] += 1

if n in _graph:
    print("Yes")
else:
    print("No")