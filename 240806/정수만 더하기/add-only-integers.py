s = input()

sum = 0
for c in s:
    if (ord(c) >= ord('0')) and (ord(c) <= ord('9')):
        sum += int(c)

print(sum)