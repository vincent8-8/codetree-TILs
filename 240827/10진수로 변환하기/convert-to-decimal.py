s = input()
digits = []
num = 0

for c in s:
    digits.append(int(c))

for i in range(len(digits)):
    num = num * 2 + digits[i]

print(num)