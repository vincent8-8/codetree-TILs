n, m, d, s = map(int, input().split())
_info = [
    list(map(int, input().split()))
    for _ in range(d)
]

_hurt_time = [
    list(map(int, input().split()))
    for _ in range(s)
]

cheese = [ 0 for _ in range(m)]

# 먹은 치즈 기록
for i in range(d):
    cheese[_info[i][1] - 1] = 1

# 특정 사람이 아픈 뒤 먹은 치즈는 제외

for i in range(s):
    people, time = _hurt_time[i]

    for j in range(d):
        if _info[j][0] == people and _info[j][2] >= time:
            cheese[_info[j][1] - 1] = 0

# 둘 중 한명이 먹지 않았다면 제외
for i in range(m):
    if cheese[i] == 0:
        continue

    did_everyone_ate = True
    
    for j in range(s):
        people, time = _hurt_time[j]
        did_everyone_ate = False

        for k in range(d):
            if _info[k][0] == people and _info[k][1] == (i + 1):
                did_everyone_ate = True
        if not did_everyone_ate:
            cheese[i] = 0
            break

max_cnt = 0

for i in range(m):
    if cheese[i] == 0:
        continue
    
    cnt = 0

    for j in range(d):
        peoples = []

        if _info[j][1] == (i + 1):
            if _info[j][0] not in peoples: 
                cnt += 1
                peoples.append(_info[j][0])
    
    max_cnt = max(max_cnt, cnt)
print(max_cnt)