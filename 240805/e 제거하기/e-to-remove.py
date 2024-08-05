s = input()

index = s.find('e')
arr = list(s)
arr.pop(index)
print("".join(arr))