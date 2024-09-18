n = int(input())
_list = [
    int(input())
    for _ in range(n)
]

avg = sum(_list) // n
blocks = 0

for i in range(n):
    if _list[i] > avg:
        blocks += 2 * (_list[i] - avg)
    elif _list[i] < avg:
        blocks += _list[i] - avg

print(blocks)