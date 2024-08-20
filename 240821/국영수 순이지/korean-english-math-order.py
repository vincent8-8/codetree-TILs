n = int(input())
_list = [
    tuple(input().split())
    for _ in range(n)
]

_list.sort(key=lambda x: (-x[1], -x[2], -x[3]))

for name, kor, eng, math in _list:
    print(name, kor, eng, math)