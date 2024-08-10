a,b = map(int, input().split())

def _sqrt(a, b):
    result = a
    for _ in range(b-1):
        result *= a
    return result


print(_sqrt(a, b))