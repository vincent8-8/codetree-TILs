n = input()
digits = []
num = 0
answer = []

for c in n:
    digits.append(int(c))

for i in range(len(digits)):
    num = num * 2 + digits[i]

num *= 17

while True:
    if num < 2:
        answer.append(num)
        break
    
    answer.append(num % 2)
    num //= 2

for digit in answer[::-1]:
    print(digit, end="")