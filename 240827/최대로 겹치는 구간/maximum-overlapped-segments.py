n = int(input())
blocks = [0] * 201

for _ in range(n):
    start, end = map(int, input().split())

    for i in range(start + 100, end + 100):
        blocks[i] += 1

print(max(blocks))