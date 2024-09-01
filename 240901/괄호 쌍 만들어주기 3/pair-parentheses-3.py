qs = input()
cnt = 0
length = len(qs)

for i in range(length):
    if qs[i] == "(":
        for j in range(i + 1, length):
            if qs[j] == ")":
                cnt += 1
print(cnt)