l = int(input())
_list = list(map(int, input().split()))

def f(n):
    for i in range(0, l):
        if n % _list[i] != 0:
            return f(n + 1)
    
    return n


print(f(1))