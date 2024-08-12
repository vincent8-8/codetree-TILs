a, sign, b = input().split()

a, b = map(int, (a, b))

def calculator(a, sign, b):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        return int(a / b)
    else:
        return False
    
result = calculator(a, sign, b)

if result:
    print(f"{a} {sign} {b} = {result}")
else:
    print("False")