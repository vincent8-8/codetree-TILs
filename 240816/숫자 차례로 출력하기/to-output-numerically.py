n = int(input())

def print_num(n):
    if n == 0:
        return 


    print_num(n-1)
    print(n, end=" ")

print_num(n)
print()
for i in range(n,0, -1):
    print(i, end=" ")