n = int(input())
_list = [
    list(input().split())
    for _ in range(n)
]
cnt = 0
ass_1_count = 0
ass_2_count = 0

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or i == k or j == k:
                continue

            ass_num = 100 * i + 10 * j + k
            ass_num = str(ass_num)
            is_answer = True

            for num, _1count, _2count in _list:
                ass_1_count = 0
                ass_2_count = 0

                if num[0] == ass_num[0]:
                    ass_1_count += 1
                elif ass_num[0] in num:
                    ass_2_count += 1

                if num[1] == ass_num[1]:
                    ass_1_count += 1
                elif ass_num[1] in num:
                    ass_2_count += 1

                if num[2] == ass_num[2]:
                    ass_1_count += 1
                elif ass_num[2] in num:
                    ass_2_count += 1
                
                if (ass_1_count != int(_1count)) or (ass_2_count != int(_2count)):
                    is_answer = False
            
            if is_answer:
                cnt += 1

print(cnt)