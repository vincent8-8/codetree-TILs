n = int(input())
_list = [ "" for _ in range(101)]
length = 0
max_len = 0

for _ in range(n):
    idx, alph = input().split()
    _list[int(idx)] = alph

for i in range(101):
    for j in range(101):
        if i + j > 101:
            break
        elif _list[i] == "" or _list[i + j - 1] == "":
            continue

        tmp_list = _list[i : i + j + 1]
        G_num = tmp_list.count("G")
        H_num = tmp_list.count("H")

        if G_num == 0 or H_num == 0:
            length = j
        elif G_num == H_num:
            length = j
        
        max_len = max(max_len, length)

print(max_len - 1)