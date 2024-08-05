s = input()
l = len(s)

print(s)

for _ in range(l):
    s = s[-1] + s[:-1]
    print(s)