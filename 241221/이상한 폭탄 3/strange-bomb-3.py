n, k = map(int, input().split())
_list = [int(input()) for _ in range(n)]
max_count = 0
max_num = 0


for standard in _list:
    if standard == -1:
        continue

    same_num_list = []
    count = 0

    for i, elem in enumerate(_list):
        if elem == standard:
            same_num_list.append(i)
            _list[i] = -1
    
    for j in range(len(same_num_list) - 1):
        if (same_num_list[j + 1] - same_num_list[j]) < k:
            count += 1
        
    if max_count == count:
        if max_num < standard:
            max_num = standard
    elif max_count < count:
        max_count = count
        max_num = standard
    else:
        continue

if max_count == 0:
    print(0)
else:
    print(max_num)