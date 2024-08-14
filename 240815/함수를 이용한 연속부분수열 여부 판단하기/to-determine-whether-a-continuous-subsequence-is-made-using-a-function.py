a, b = map(int, input().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

def discriminate(a, b):
    for i in range(0, a - b + 1):
        if a_list[i:i+b] == b_list:
            return True
    return False




if discriminate(a, b):
    print("Yes")
else:
    print("No")