OFFSET = 10000

n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
max_area = 0

for i in range(n):
    _list[i][0] += OFFSET
    _list[i][1] += OFFSET

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == k or i == k or j == k:
                continue
            
            if _list[i][0] == _list[j][0] and _list[i][0] != _list[k][0]:
                if _list[i][1] == _list[k][1] or _list[i][1] != _list[j][1]:
                    area = abs(_list[i][0] - _list[k][0]) * abs( _list[i][1] - _list[j][1])
                    
                    max_area = max(max_area, area)
print(max_area)