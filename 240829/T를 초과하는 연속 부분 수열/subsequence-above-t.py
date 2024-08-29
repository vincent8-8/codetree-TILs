n, t = map(int, input().split())
_list = list(map(int, input().split()))

cnt = 0
max_cnt = 0

for i in range(n):

    if i == 0:

        if _list[0] > t:
            cnt = 1
        else:
            cnt = 0

        continue
    
    if _list[i] <= t:
        if max_cnt < cnt:
            max_cnt = cnt
        cnt = 0
        continue
    
    cnt += 1

if(max_cnt == 0):
    print(cnt)
else:
    print(max_cnt)