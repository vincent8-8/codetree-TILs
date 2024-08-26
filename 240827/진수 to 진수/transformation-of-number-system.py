a, b = map(int, input().split())
n = input()

digits_a = []
digits_b = []

num = 0
for c in n:
    num = num * a + int(c)

while True:
    if num < b:
        digits_b.append(num)
        break
    
    digits_b.append(num % b)
    num //= b

for digit in digits_b[::-1]:
    print(digit, end="")