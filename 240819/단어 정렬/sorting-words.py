n = int(input())
_list = [
    input() for _ in range(n)
]

_list = sorted(_list)
for elem in _list:
    print(elem)