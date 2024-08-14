y, m , d = map(int, input().split())

def is_leap_year(y):
    if y % 4 == 0:
        if y % 400 == 0:
            return True
        elif y % 100 == 0:
            return False
        return True
    return False

def season(m):
    if 3 <= m <= 5:
        print("Spring")
    elif 6 <= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Fall")
    else:
        print("Winter")

def discriminate(y, m , d):
    if m == 4 or m == 6 or m == 9 or m == 11:
        if d > 30:
            return False
    elif m == 2:
        if  is_leap_year(y):
            if d > 29:
                return False
        else:
            if d > 28:
                return False
    
    return True


if discriminate(y, m, d):
    season(m)
else:
    print("-1")