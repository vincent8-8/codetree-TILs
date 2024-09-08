import sys
n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
area = 0
min_area = sys.maxsize

for _ in range(n):
    except_dot = _list.pop(0)
    
    h = max(_list[0][1], _list[1][1], _list[2][1]) - min(_list[0][1], _list[1][1], _list[2][1])
    w = max(_list[0][0], _list[1][0], _list[2][0]) - min(_list[0][0], _list[1][0], _list[2][0])
    area = h * w

    if area < min_area:
        min_area = area

    _list.append(except_dot)
print(min_area)