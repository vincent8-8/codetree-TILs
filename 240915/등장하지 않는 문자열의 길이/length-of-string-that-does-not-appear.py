n = int(input())
s = input()

min_len = n

def search(length):
    for i in range(n - length):
        target = s[i : i + length]
        
        if ( target in s[0:i] ) or ( target in s[i + 1:] ):
            return False

    return True 

for i in range(1, n):
    if search(i):
        min_len = i
        break

print(min_len)