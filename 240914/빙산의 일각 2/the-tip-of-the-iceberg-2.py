n = int(input())
_list = [
    int(input())
    for _ in range(n)
]
max_cnt = 0

for h in range(1, 1001):
    before_status = 0
    cnt = 0
    for i in range(n):
        if _list[i] > h:
            if before_status == 0:
                cnt += 1
                before_status = 1
        else:
            before_status = 0
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)