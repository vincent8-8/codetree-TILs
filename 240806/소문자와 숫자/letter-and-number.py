s = input()

for c in s:
    if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
        print(c.lower(), end="")
    elif (ord(c) >= ord('0')) and (ord(c) <= ord('9')):
        print(c, end="")