n = int(input())

before = list(map(int, input().split()))
after = list(map(int, input().split()))
cost = 0

for i in range(n - 1, -1, -1):
    if before[i] < after[i]:
        need = after[i] - before[i]

        for j in range(i - 1, -1, -1):
            if need == 0:
                break
            elif before[j] <= need:
                before[i] += before[j]
                cost += before[j] * (i - j)
                need -= before[j]
                before[j] = 0
            elif before[j] > need:
                before[i] += need
                cost += need * (i - j)
                before[j] -= need
                need = 0
print(cost)