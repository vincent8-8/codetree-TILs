n = int(input())
_list = list(input().split())

for i in range(len(_list)):
    _list[i] = ord(_list[i]) - 65
cost = 0
idx = 0

while True:
    if idx == len(_list) - 1:
        idx = 0
    
    if _list[idx] > _list[idx + 1]:
        tmp = _list[idx]
        _list[idx] = _list[idx + 1]
        _list[idx + 1] = tmp
        
        cost += 1
    
    if _list == sorted(_list):
        break
    else:
        idx += 1

print(cost)