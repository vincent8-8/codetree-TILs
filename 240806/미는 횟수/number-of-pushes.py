a = input()
b = input()

cnt = 0

while a != b:
    cnt += 1
    a = a[-1] + a[:-1]
    if cnt == len(a):
        print("-1")
        break
        
if cnt != len(a):
    print(cnt)