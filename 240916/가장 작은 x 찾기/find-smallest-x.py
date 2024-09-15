n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

for i in range(1, 10001):
    curr = i * 2
    find_answer = True

    for a, b in _list:
        if not (a <= curr <= b):
            find_answer = False
            break
        curr *= 2

    if find_answer:
        print(i)
        break