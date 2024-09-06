n = int(input())
_list = [ "" for _ in range(101)]
length = 0
max_len = 0

for _ in range(n):
    idx, alph = input().split()
    _list[idx] = alph

for i in range(101):
    for j in range(101):
        if i + j > 101:
            break

        tmp_list = _list[i, i + j + 1]

        if (not "G" in tmp_list) and (not "H" in tmp_list):
            continue
        elif (not "G" in tmp_list) or (not "H" in tmp_list):
            length = j
        elif (tmp_list.count("G")) == (tmp_list.count("H")):
            length = j
        
        max_len = max(max_len, length)

print(max_len)