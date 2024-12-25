a, b = map(int, input().split())
c, d = map(int, input().split())

section = [0] * 101

for i in range(a, b):
    section[i] = 1

for i in range(c, d):
    section[i] = 1

print(section.count(1))