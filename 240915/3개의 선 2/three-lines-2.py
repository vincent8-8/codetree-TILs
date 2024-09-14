n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

is_answer = 0

def check_answer_x(x1, y1, x2):
    for x, y in _list:
        if not ( x in (x1, x2) or (y == y1) ):
            return 0
    return 1

def check_answer_y(x1, y1, y2):
    for x, y in _list:
        if not ( (x == x1) or y in (y1, y2) ):
            return 0
    return 1

def check_answer_all_x(x1, x2, x3):
    for x, y in _list:
        if not x in (x1, x2, x3):
            return 0
    return 1

def check_answer_all_y(y1, y2, y3):
    for x, y in _list:
        if not x in (y1, y2, y3):
            return 0
    return 1


for i in range(11):
    for j in range(11):
        for k in range(11):
            if is_answer == 1:
                break

            is_answer = max(check_answer_x(i, j, k), check_answer_y(i, j, k), check_answer_all_x(i, j, k), check_answer_all_y(i, j, k))
        
        if is_answer == 1:
            break

    if is_answer == 1:
        break

print(is_answer)