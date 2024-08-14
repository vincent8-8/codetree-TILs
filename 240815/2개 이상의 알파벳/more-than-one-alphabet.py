A = input()

def discriminate(s):
    for i in range(len(s)):
        if s[0] != s[i]:
            return True
    return False

if discriminate(A):
    print("Yes")
else:
    print("No")