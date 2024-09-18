n = int(input())
_list = [
    int(input())
    for _ in range(n)
]

avg = sum(_list) // n
cnt = 0

while True:
    is_changed = False

    for i in range(n):
        if _list[i] > avg:
            _list[i] -= 1
            break
    for i in range(n):
        if _list[i] < avg:
            _list[i] += 1
            is_changed = True
            break
    
    if is_changed:
        cnt += 1
    else:
        break

print(cnt)