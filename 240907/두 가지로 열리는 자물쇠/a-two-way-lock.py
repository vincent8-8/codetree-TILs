n = int(input())
c1 = list(map(int, input().split()))
c2 = list(map(int, input().split()))
cnt = 0

def discriminate_c1(x, y, z):
    if (abs(c1[0] - x) % (n - 2)) <= 2 and (abs(c1[1] - y) % (n - 2)) <= 2 and (abs(c1[2] - z) % (n - 2)) <= 2:
        return True
    else:
        return False
    
def discriminate_c2(x, y, z):
    if (abs(c2[0] - x) % (n - 2)) <= 2 and (abs(c2[1] - y) % (n - 2)) <= 2 and (abs(c2[2] - z) % (n - 2)) <= 2:
        return True
    else:
        return False

for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if discriminate_c1(i, j, k):
                cnt += 1
            elif discriminate_c2(i, j, k):
                cnt += 1

print(cnt)