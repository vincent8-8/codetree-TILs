n = int(input())
_list = list(input())
maxOfMin = -1

for i in range(n):
    if _list[i] == '1':
        continue
    for j in range(i + 1, n):
        if _list[j] == '1':
            continue
        min_dist = 101

        _list[i] = '1'
        _list[j] = '1'

        indices_of_1 = [k for k, elem in enumerate(_list) if elem == '1']
        
        for l in range(len(indices_of_1) - 1):
            local_dist = indices_of_1[l + 1] - indices_of_1[l]
            min_dist = min(local_dist, min_dist)
        
        maxOfMin = max(min_dist, maxOfMin)

        _list[i] = '0'
        _list[j] = '0'

print(maxOfMin)
