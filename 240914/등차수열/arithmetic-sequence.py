n = int(input())
_list = list(map(int, input().split()))
length = len(_list)

max_cnt = 0

for i in range(101):
    cnt = 0
    for j in range(length):
        for k in range(j + 1, length):
            if (2 * i) == (_list[j] + _list[k]):
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)

print(max_cnt)