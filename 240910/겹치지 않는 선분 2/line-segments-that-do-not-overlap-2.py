OFFSET = 1000000
MAX_SIZE = 2000001

n = int(input())

_list = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = 0


for i in range(n):
    is_answer = True

    std_start, std_end = _list[i]
    std_start += OFFSET
    std_end += OFFSET

    for j in range(n):
        if i == j:
            continue

        counter_start = _list[j][0] + OFFSET
        counter_end = _list[j][1] + OFFSET

        if counter_start <= std_start <= counter_end and counter_start <= std_end <= counter_end:
            is_answer = False
            break
        
        if std_start <= counter_start and counter_end <= std_end:
            is_answer = False
            break

    if is_answer:
        cnt += 1
print(cnt)