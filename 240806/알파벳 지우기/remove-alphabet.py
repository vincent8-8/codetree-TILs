a = input()
b = input()

a_i = ""
b_i = ""

for c in a:
    if (ord(c) >= ord('0')) and (ord(c) <= ord('9')):
        a_i += c

for c in b:
    if (ord(c) >= ord('0')) and (ord(c) <= ord('9')):
        b_i += c

print(int(a_i) + int(b_i))