n, m = map(int, input().split())
_list = list(map(int, input().split()))
cnt = 0

for i in range(n):
    if cnt == 0 and i == m:
        cnt += 1
    elif i == (1 + m * 2) * cnt:
        cnt += 1

people = _list.count(1)

if people == 0:
    print(0)
elif m == 0:
    print(people)
else:
    print(cnt)