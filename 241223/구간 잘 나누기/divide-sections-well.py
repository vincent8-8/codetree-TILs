import sys

n, m = map(int, input().split())
_list = list(map(int, input().split()))

ans = 10000

for i in range(1, n * 100 + 1):
    
    possible = True
    section = 1
    cnt = 0

    for j in range(n):
        if _list[j] > i :
            possible = False
            break
        
        if cnt + _list[j] > i:
            cnt = 0
            section += 1
        
        cnt += _list[j]
    
    if possible and section <= m:
        ans = min(ans, i)

print(ans)