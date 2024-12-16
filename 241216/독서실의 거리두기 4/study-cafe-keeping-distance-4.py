n = int(input())
_list = list(input())

zero_pos = []
maxOfMin = -1

for i, elem in enumerate(_list):
    if elem == "0":
        zero_pos.append(i)

for zero_1 in zero_pos:
    for zero_2 in zero_pos:
        if zero_1 == zero_2:
            continue
        
        distance = 999
        
        after_sit_list = _list
        after_sit_list[zero_1] = "1"
        after_sit_list[zero_2] = "1"

        indices_1 = [i for i, x in enumerate(after_sit_list) if x == "1"]

        for i in range(len(indices_1) - 1):
            local_distance = indices_1[i + 1] - indices_1[i]
            distance = min(local_distance, distance)
        
        maxOfMin = max(distance, maxOfMin)

print(maxOfMin + 1)