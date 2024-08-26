m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
elapsed_1 = 0
elapsed_2 = 0

for i in range(m1):
    elapsed_1 += num_of_days[i]
elapsed_1 += d1

for i in range(m2):
    elapsed_2 += num_of_days[i]
elapsed_2 += d2

index = 1

if elapsed_2 - elapsed_1 > 0:
    for _ in range(elapsed_2 - elapsed_1):
        index += 1
        if index > 6:
            index -= 6
elif elapsed_2 - elapsed_1 < 0:
    for _  in range(abs(elapsed_2 - elapsed_1)):
        index -= 1
        if index < 0:
            index += 7

print(days[index])