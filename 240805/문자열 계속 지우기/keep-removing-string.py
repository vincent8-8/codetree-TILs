a = input()
b = input()

index = a.find(b)

while index != -1:
    index = a.find(b)
    a = a[0:index] + a[index+len(b):]

print(a)