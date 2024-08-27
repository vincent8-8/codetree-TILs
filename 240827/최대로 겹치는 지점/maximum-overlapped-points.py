n = int(input())
blocks = [0] * 101

for _ in range(n):
    s, e = map(int, input().split())

    for i in range(s, e+1):
        blocks[i] += 1

print(max(blocks))