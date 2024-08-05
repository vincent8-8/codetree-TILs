a, b = input().split()

a_i = ""
b_i = ""

for c in a:
    if (ord(c) >= ord('0')) and (ord(c) <= ord('9')):
        a_i += c
    else:
        break

for c in b:
    if (ord(c) >= ord('0')) and (ord(c) <= ord('9')):
        b_i += c
    else:
        break

print(int(a_i) + int(b_i))