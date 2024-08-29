n = int(input())
_list = [
    int(input())
    for _ in range(n)
]

cnt = 0
max_cnt = 0

for i in range(n):
    if i == 0:
        cnt = 1
        continue
    
    if _list[i] * _list[i - 1] < 0:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 1
        continue
    
    cnt += 1

if(max_cnt == 0):
    print(cnt)
else:
    print(max_cnt)