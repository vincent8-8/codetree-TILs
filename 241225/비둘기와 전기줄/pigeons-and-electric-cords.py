n = int(input())
_list = [list(map(int, input().split())) for _ in range(n)]
answer = 0

for i in range(1, 11):
    last_pos = -1
    for elem in _list:
        if elem[0] == i:
            if last_pos == -1:
                last_pos = elem[1]
            else:
                if last_pos != elem[1]:
                    answer += 1
                    last_pos = elem[1]

print(answer)