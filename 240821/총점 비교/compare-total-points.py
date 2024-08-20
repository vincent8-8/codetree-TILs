n = int(input())
_list = [
    tuple(input().split())
    for _ in range(n)
]

_list.sort(key=lambda x: (int(x[1]) + int(x[2]) + int(x[3])))

for name, s1, s2, s3 in _list:
    print(name, s1, s2, s3)