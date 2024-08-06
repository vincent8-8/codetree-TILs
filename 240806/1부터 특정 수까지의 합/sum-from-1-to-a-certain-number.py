n = int(input())

def quotient(n):
    s = 0
    for i in range(n+1):
        s += i
    
    return s // 10

print(quotient(n))