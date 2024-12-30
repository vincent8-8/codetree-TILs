n = int(input())
_list = list(map(int, input().split()))

sorted_list = sorted(_list)
min_value = sorted_list[0]
answer = 0

for i in range(1, n):
    if min_value != sorted_list[i]:
        answer = i
        break
    
if len(sorted_list) > 3 and sorted_list[answer] == sorted_list[answer + 1]:
    print(-1)
else:
    sec_min = sorted_list[answer]

    for i in range(n):
        if _list[i] == sec_min:
            print(i + 1)
            break