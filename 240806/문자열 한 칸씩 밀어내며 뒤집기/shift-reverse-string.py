s, n = input().split()

for _ in range(int(n)):
    q = int(input())

    if q == 1:
        s = s[1:] + s[0]
        print(s)
    elif q == 2:
        s = s[-1] + s[:-1]
        print(s)
    else:
        s = s[::-1]
        print(s)