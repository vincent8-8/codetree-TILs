n, m = map(int, input().split())
_list = list(map(int, input().split()))
cnt = 0
last = 0

for i in range(n):
    if _list[i] == 1:
        if cnt == 0:
            cnt += 1
            last = i
        elif last - m > i or last + m < i:
            cnt += 1
            last = i + m

people = _list.count(1)

if people == 0:
    print(0)
elif m == 0:
    print(people)
else:
    print(cnt)