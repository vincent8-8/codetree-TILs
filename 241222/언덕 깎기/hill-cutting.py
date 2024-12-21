n = int(input())
_list = [int(input()) for _ in range(n)]
answer = [0] * 84

for i in range(0, 84):
    for elem in _list:
        changed = 0

        if elem > (i + 17):
            changed =  (elem - (i + 17)) ** 2
        elif elem < i:
            changed =  (i - elem) ** 2
        
        answer[i] += changed

print(min(answer))