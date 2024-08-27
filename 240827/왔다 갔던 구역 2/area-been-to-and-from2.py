n = int(input())
blocks = [0] * 1001
start = 500
pre = ""

for _ in range(n):
    x, direction = input().split()
    
    if direction == "L":
        if pre == "R":
            blocks[start] -= 1

        for _ in range(int(x)):
            blocks[start] += 1 
            start -= 1
        pre = "L"

    else:
        if pre == "L":
            blocks[start] -= 1
            
        for _ in range(int(x)):
            blocks[start] += 1
            start += 1

cnt = 0

for i in range(1001):
    if blocks[i] >= 2:
        cnt += 1

print(cnt)