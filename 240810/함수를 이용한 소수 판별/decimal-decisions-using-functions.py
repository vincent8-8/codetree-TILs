a, b = map(int, input().split())

def is_prime(n):
    for i in range(1, n):
        if i != 1:
            if n % i == 0:
                return False
    return True

sum = 0

for i in range(a, b+1):
    if is_prime(i):
        sum += i

print(sum)