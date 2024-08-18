n = int(input())
_list = list(map(int, input().split()))

_list.sort()

for elem in _list:
    print(elem, end=" ")

print()

for elem in _list[::-1]:
    print(elem, end=" ")