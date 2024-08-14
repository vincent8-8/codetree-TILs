m, d = map(int, input().split())

def discriminate(m, d):
    if d > 31:
        return False
    elif m > 12:
        return False
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False
    elif m == 2:
        if d > 28:
            return False
    return True

if discriminate(m, d):
    print("Yes")
else:
    print("No")