n = int(input())
blocks = [ [0, 0, 0] for _ in range(2001)]
start = 500

for _ in range(n):
    x, direction = input().split()
    
    if direction == "L":

        for _ in range(int(x)):
            blocks[start][0] = 1 
            blocks[start][1] += 1
            start -= 1
        start += 1

    else:

        for _ in range(int(x)):
            blocks[start][0] = 2 
            blocks[start][2] += 1
            start += 1
        start -= 1

cnt_gray = 0
cnt_black = 0 
cnt_white = 0

for i in range(2001):
    if blocks[i][1] >= 2 and blocks[i][2] >= 2:
        cnt_gray += 1
    elif blocks[i][0] == 1:
        cnt_white += 1
    elif blocks[i][0] == 2:
        cnt_black += 1

print(cnt_white, cnt_black, cnt_gray)