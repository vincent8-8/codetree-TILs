n = int(input())

def print_func(n):
    start = 1

    for i in range(n):
        for j in range(n):
            if start % 9 != 0:
                print(start % 9, end=" ")
            else:
                print("9", end=" ")
            
            start += 1
        
        print()

print_func(n)