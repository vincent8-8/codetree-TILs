n = int(input())
_list = list(map(int, input().split()))

# 중복을 찾는 방법은 리스트를 set으로 변환하는 방법을 사용해 길이가 n-1 이 맞는지 확인한다.

for start in range(1, _list[0]):
    answer = [start]

    for i in range(n-1):
        answer.append(_list[i] - answer[-1])
        if answer[-1] < 0:
            break

    answer_set = set(answer)
    answer_set = sorted(answer_set)

    if answer_set[0] <= 0:
        continue
    elif len(answer_set) != n:
        continue
    
for elem in answer:
    print(elem, end=" ")