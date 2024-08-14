s = input()

def palindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False

if palindrom(s):
    print("Yes")
else:
    print("No")