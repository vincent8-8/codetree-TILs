n = int(input())
_list = [
    input()
    for _ in range(n)
]

max_sum = 0
_sum = 0


for i in range(n):
    condition = True
    length_A = len(_list[i])
    
    for j in range(i + 1, n):
        condition = True
        length_B = len(_list[j])
        min_len_1 = min(length_A, length_B)

        for idx in range(-1, -(min_len_1 + 1), -1):
                tmp = int(_list[i][idx]) + int(_list[j][idx])
                if tmp > 9:
                    condition = False
                    break

        if condition:
             _sum = int(_list[i]) + int(_list[j])
        else:
            continue

        for k in range(j + 1, n):
            condition = True
            _sum = str(_sum)

            length_sum = len(_sum)
            length_C = len(_list[k])
            min_len_2 = min(length_sum, length_C)

            for idx in range(-1, -(min_len_2 + 1), -1):
                tmp = int(_sum[idx]) + int(_list[k][idx])
                if tmp > 9:
                    condition = False
                    break

            if condition:
                _sum = int(_sum) + int(_list[k])
                if max_sum < _sum:
                    max_sum = _sum
print(max_sum)