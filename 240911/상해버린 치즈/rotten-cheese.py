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

print(cheese)