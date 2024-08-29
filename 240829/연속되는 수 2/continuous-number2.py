n = int(input())
_list = [
    int(input())
    for _ in range(n)
]

cnt = 0
max_cnt = 0

for i in range(n):
    if i == 0 or _list[i] == _list[i - 1]:
        cnt += 1
    else:
        if max_cnt < cnt:
            max_cnt = cnt
            cnt = 1
    
print(max_cnt)