n = int(input())
_lines = [list(map(int, input().split())) for _ in range(n)]
find_answer = "No"

for i in range(n):
    _graph = [0] * 101

    for j in range(n):
        if i == j:
            continue
        
        a, b = _lines[j][0], _lines[j][1]
        for k in range(a, b + 1):
            _graph[k] += 1

    if (n - 1) in _graph:
        find_answer = "Yes"

print(find_answer)