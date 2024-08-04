n = int(input())

s = input().split()

string = ""

for elem in s:
    string += elem

cnt = 0

for elem in string:
    if cnt % 5 != 0 or cnt == 0:
        cnt += 1
        print(elem, end="")
    else:
        print()
        print(elem, end="")
        cnt += 1