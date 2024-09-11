k, n = map(int, input().split())
_list = [
    list(map(int, input().split()))
    for _ in range(k)
]

cnt = 0

for i in range(1, n + 1): # 1 ~ 4
    for j in range(i + 1, n + 1): # 2 ~ 4
        state = ""
        is_changed = False

        for l in range(k):
            if _list[l].index(i) > _list[l].index(j):
                if state == "<":
                    is_changed = True
                    break
                else:
                    state = ">"
            else:
                if state == ">":
                    is_changed = True
                    break
                else:
                    state = "<"
        
        if not is_changed:
            cnt += 1
print(cnt)