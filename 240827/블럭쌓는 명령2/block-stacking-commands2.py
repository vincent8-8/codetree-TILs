n, k = map(int, input().split())

_list = [
    tuple(map(int, input().split()))
    for _ in range(k)
]

blocks = [0] * n

for elem in _list:
    for i in range(elem[0], elem[1]+1):
        blocks[i] += 1

print(max(blocks))