n = int(input())
_list = [
    input()
    for _ in range(n)
]

_max_sum = 0
_sum = 0
_tmp = 0

for i in range(n):
    _sum = _list[i]
    _cnt = 0

    for j in range(i + 1, n):
        _sum = str(_sum)
        _length_A = len(_sum)
        _length_B = len(_list[j])
        condition = True
        
        if _length_A >= _length_B:
            for k in range(-1, -(_length_B) - 1, -1):
                _tmp = int(_sum[k]) + int(_list[j][k])
                if _tmp > 9:
                    condition = False
                    break
        else:
            for k in range(-1, -(_length_A) - 1, -1):
                _tmp = int(_sum[k]) + int(_list[j][k])
                if _tmp > 9:
                    condition = False
                    break

        if condition:
            _cnt += 1
            _sum = int(_sum) + int(_list[j])
            if _cnt == 2:
                break
    

    _sum = int(_sum)

    if _cnt == 2 and _sum >_max_sum:
        _max_sum = _sum

if _max_sum == 0:
    print("-1")
else:
    print(_max_sum)