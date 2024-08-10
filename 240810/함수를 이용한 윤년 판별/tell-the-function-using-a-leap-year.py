y = int(input())

def dicriminate(n):
    if (n % 100 == 0) and (n % 400 != 0):
        return False
    if n % 4 != 0:
        return False
    return True

if dicriminate(y):
    print("true")
else:
    print("false")