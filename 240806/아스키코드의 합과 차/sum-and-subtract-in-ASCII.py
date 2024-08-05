a, b = input().split()

a_ord = ord(a)
b_ord = ord(b)

print(a_ord + b_ord, end=" ")

if a <= b:
    print(b_ord - a_ord)
else:
    print(a_ord - b_ord)