str1 = input()
str2 = input()

if len(str1) > len(str2):
    print(str1, len(str1))
elif len(str1) < len(str2):
    print(str2, len(str2))
else:
    print("same")