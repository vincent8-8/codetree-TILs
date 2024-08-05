a = input()
b = input()

index = a.find(b)
length = len(b)

while index != -1:
    arr = list(a)
    del arr[index : index + length]
    a = "".join(arr)
    index = a.find(b)

print(a)