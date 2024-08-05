a, b = input().split()

s = str(int(a) + int(b))

cnt = 0

for c in s:
    if c == '1':
        cnt += 1

print(cnt)