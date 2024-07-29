str1 = input()
letter = input()

cnt = 0

for elem in str1:
    if elem == letter:
        cnt += 1

print(cnt)