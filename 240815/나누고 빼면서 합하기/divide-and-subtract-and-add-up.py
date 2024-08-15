n, m = map(int, input().split())
_list = list(map(int, input().split()))
result = 0

def calculate():
    global m, result
    
    while m >= 1:
        result += _list[m-1]

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
        
    return result


print(calculate())