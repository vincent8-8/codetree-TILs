n = int(input())
_list = [list(map(int, input().split())) for _ in range(n)]
answer = 0
_list.sort()

for i in range(n):
    count = 0
    last_pos = _list[i][1]
    for j in range(i + 1, n):
        if _list[i][0] != _list[j][0]:
            break
        
        if last_pos != _list[j][1]:
            count += 1
            last_pos = _list[j][1]
        
    answer += count

print(answer)