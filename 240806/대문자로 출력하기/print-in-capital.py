s = input()

for c in s:
    if (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
        print(c.upper(), end="")