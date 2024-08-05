s = input()

for c in s:
    if (ord(c) >= ord('A')) and (ord(c) <= ord('Z')):
        print(c.lower(), end="")
    elif (ord(c) >= ord('a')) and (ord(c) <= ord('z')):
        print(c.upper(), end="")