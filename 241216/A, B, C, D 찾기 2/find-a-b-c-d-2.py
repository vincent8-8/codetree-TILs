_list = list(map(int, input().split()))

_list.sort()
length = len(_list)
a = _list[0]
b = _list[1]
c = 0
d = 0

def find_answer(a, b, c, d):
    if (a + b + c + d) in _list:
        if (a + b + c) in _list and (b + c + d) in _list: 
            if (c + d) in _list:
                return True
    return False

for i in range(2, length//2):
    c = _list[i]
    for j in range(3, length//2):
        d = _list[j]
        found = find_answer(a, b, c, d)
        if found:
            break
    if found:
        break

print(a, b, c, d)
    