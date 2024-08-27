n = int(input())
blocks = [0] * 200001
curr = 100000

for _ in range(n):
    x, d = input().split()

    if d == "L":
        for _ in range(int(x)):
            blocks[curr] = 1   # 1 means white
            curr -= 1
        curr += 1
    else:
        for _ in range(int(x)):
            blocks[curr] = 2   # 2 means black
            curr += 1
        curr -= 1

cnt_white = 0
cnt_black = 0

for i in range(200001):
    if blocks[i] == 1:
        cnt_white += 1
    elif blocks[i] == 2:
        cnt_black += 1

print(cnt_white, cnt_black)