digits = list(input())
len_digits = len(digits)
answer = 0

if "0" in digits:
    for i in range(len_digits):
        if digits[i] == "0":
            digits[i] = "1"
            break
else:
    digits[-1] = 0

digits = digits[::-1]

for i in range(len_digits):
    answer += (2 ** i) * int(digits[i])
print(answer)