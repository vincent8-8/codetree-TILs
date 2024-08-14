a, b = map(int, input().split())

def discriminate(n):
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            return False
    
    if ((n // 100) + ((n % 100) // 10) + (n %  10)) % 2 == 0:
        return True
    else: 
        return False
    
cnt = 0

for i in range(a, b+1):
    if discriminate(i):
        cnt += 1

print(cnt)