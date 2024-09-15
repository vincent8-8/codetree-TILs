n = int(input())
seats = input()

max_d = 0

for i in range(n):
    if seats[i] == "1":
        continue

    left_person = 0
    right_person = n
    local_min = 0

    for j in range(i):
        if seats[j] == "1":
            left_person = max(left_person, j)
        
    left_d = i - left_person
    
    for k in range(i + 1, n):
        if seats[k] == "1":
            right_person = min(right_person, k)
    
    right_d = right_person - i
        
    local_min = min(left_d, right_d)

    max_d = max(local_min, max_d)

print(max_d)