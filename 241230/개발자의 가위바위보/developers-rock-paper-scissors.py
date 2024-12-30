n = int(input())
_list = [list(map(int, input().split())) for _ in range(n)]

def r_s_p(_rsp):
    count = 0

    for elem in _list:
        if _rsp[elem[0] - 1] == '주먹' and _rsp[elem[1] - 1] == "가위":
            count += 1
        elif _rsp[elem[0] - 1] == '가위' and _rsp[elem[1] - 1] == "보":
            count += 1
        elif _rsp[elem[0] - 1] == '보' and _rsp[elem[1] - 1] == "주먹":
            count += 1
    
    return count

round_count = []

round_count.append(r_s_p(['주먹', '가위', '보']))
round_count.append(r_s_p(['주먹', '보', '가위']))
round_count.append(r_s_p(['가위', '바위', '보']))
round_count.append(r_s_p(['가위', '보', '바위']))
round_count.append(r_s_p(['보', '가위', '바위']))
round_count.append(r_s_p(['보', '바위', '가위']))

print(max(round_count))
