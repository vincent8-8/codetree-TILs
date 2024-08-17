l = int(input())
_list = list(map(int, input().split()))
step = min(_list)

def f(n):
    for i in range(0, l):
        if n % _list[i] != 0:
            return f(n + step)
    
    return n


print(f(1))