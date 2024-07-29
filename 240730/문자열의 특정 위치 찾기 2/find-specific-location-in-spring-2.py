arr = ["apple", "banana", "grape", "blueberry", "orange"]
letter = input()

cnt = 0

for elem in arr:
    if letter == elem[2] or letter == elem[3]:
        print(elem) 
        cnt += 1
print(cnt)