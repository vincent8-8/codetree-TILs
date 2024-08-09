n = int(input())

def discriminant(n):
    return (n % 2 == 0) and (((n // 10) + (n % 10)) % 5 == 0)

if discriminant(n):
    print("Yes")
else:
    print("No")