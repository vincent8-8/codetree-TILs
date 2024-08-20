n = int(input())
_list = [
    tuple(input().split())
    for _ in range(n)
]

_list.sort(key=lambda x: x[1])

for name, cm, kg in _list:
    print(name, cm, kg)