import sys
n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
area = 0
min_area = sys.maxsize

for i in range(n):
    _list.sort(key=lambda x: x[0])
    except_dot = _list.pop(i)

    w = _list[-1][0] - _list[0][0]

    _list.sort(key=lambda x: x[1])
    h = _list[-1][1] - _list[0][1]

    area = w * h
    
    if area < min_area:
        min_area = area

    _list.append(except_dot)
print(min_area)