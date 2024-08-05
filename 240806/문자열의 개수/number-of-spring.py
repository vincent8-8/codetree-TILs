s = input()
cnt = 1
arr = []

while s != '0':
    if (cnt % 2) != 0:
        arr.append(s)
    s = input()
    cnt += 1

print(cnt-1)
for elem in arr:
    print(elem)