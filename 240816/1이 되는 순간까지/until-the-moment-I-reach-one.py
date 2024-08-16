n = int(input())
cnt = 0

def f(n):
    global cnt

    r = n % 10
    if n == 1:
        return

    if r % 2 == 0:
        cnt += 1
        return f(n // 2)
    else:
        cnt += 1
        return f(n//3)

f(n)
print(cnt)