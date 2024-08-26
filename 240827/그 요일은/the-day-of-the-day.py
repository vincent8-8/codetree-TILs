m1, d1, m2, d2 = map(int, input().split())
day = input()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

elapsed_days_1 = 0
elapsed_days_2 = 0
answer = 0

for i in range(m1):
    elapsed_days_1 += num_of_days[i]
elapsed_days_1 += d1

for i in range(m2):
    elapsed_days_2 += num_of_days[i]
elapsed_days_2 += d2

diff = elapsed_days_2 - elapsed_days_1
answer = diff // 7

index = 1
for i in range(diff % 7):
    index += 1
    if days[index] == day:
        answer += 1
    if index > 6:
        index -= 7

print(answer)