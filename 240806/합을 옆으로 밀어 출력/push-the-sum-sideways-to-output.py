n = int(input())

sum = 0

for _ in range(n):
    i = int(input())
    sum += i

sum = str(sum)
print(sum[1:] + sum[0])