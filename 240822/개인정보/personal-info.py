_list = [
    tuple(input().split())
    for _ in range(5)
]

_list.sort(key=lambda x: x[0])

print("name")
for name, h, w in _list:
    print(name, h, w)

_list.sort(key=lambda x: -int(x[1]))

print()
print("height")
for name, h, w in _list:
    print(name, h, w)