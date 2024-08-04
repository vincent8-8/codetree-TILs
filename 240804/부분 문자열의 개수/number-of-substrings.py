s = input()
t = input()

cnt = 0

for i in range(len(s) - 1):
    if s[i:i+2] == t:
        cnt += 1

print(cnt)