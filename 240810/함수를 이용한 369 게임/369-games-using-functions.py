a, b = map(int, input().split())

def is_3_6_9(n):
    num_str = str(n)
    return ('3' in num_str) or ('6' in num_str) or ('9' in num_str)

cnt = 0

for i in range(a, b+1):
    if i % 3 == 0 or is_3_6_9(i):
        cnt += 1

print(cnt)