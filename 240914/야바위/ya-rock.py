n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0

for i in range(1, 4):
    pos = i
    cnt = 0
    for a, b, c in _list:
        if a == pos:
            pos = b
            if c == pos:
                cnt += 1
            else:
                continue
        elif b == pos:
            pos = a
            if c == pos:
                cnt += 1
            else:
                continue
        else:
            if c == pos:
                cnt += 1
    
    max_cnt = max(max_cnt, cnt)
print(max_cnt)