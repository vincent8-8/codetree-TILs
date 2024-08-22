n = int(input())

_list = [
    tuple(input().split())
    for _ in range(n)
]

_list.sort(key=lambda x: (int(x[1]), -int(x[2])))

for name, h, w in _list:
    print(name, h, w)