n = int(input())
_list = [int(input()) for _ in range(n)]

avg = sum(_list) // len(_list)
cost = 0

if avg > 50:
    for i, elem in enumerate(_list):
        if elem < avg - 17:
            cost += (avg - 17) - elem
        elif elem > avg:
            cost += elem - avg
else:
    for i, elem in enumerate(_list):
        if elem > avg + 17:
            cost += elem - (avg - 17)
        elif elem < avg:
            cost += avg - elem

print(cost - n)