import sys

n = int(input())
seats = list(input())

max_d = 0

for i in range(n):
    if seats[i] == "1":
        continue
    
    seats[i] = "1"

    before_1 = -1
    local_min = sys.maxsize
    dist = 0
    for j in range(n):
        if seats[j] == "1":
            if before_1 == -1:
                before_1 = j
                continue
            else:
                dist = j - before_1
                before_1 = j
            
            local_min = min(local_min, dist)
        
    max_d = max(local_min, max_d)

    seats[i] = "0"

print(max_d)