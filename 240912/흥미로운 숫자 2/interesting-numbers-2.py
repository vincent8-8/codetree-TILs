x, y = map(int, input().split())

cnt = 0

for i in range(x, y + 1):
    num_to_str = str(i)
    str_to_list = list(num_to_str)

    str_to_list.sort()
    if str_to_list[0] == str_to_list[-2] and str_to_list[0] != str_to_list[-1]:
        cnt += 1
    elif str_to_list[0] != str_to_list[1] and str_to_list[1] == str_to_list[-1]:
        cnt += 1
print(cnt)