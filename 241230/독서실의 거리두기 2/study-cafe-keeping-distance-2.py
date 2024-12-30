n = int(input())
_input = input()
seats = []
min_distance = []

for i in range(len(_input)):
    seats.append(int(_input[i]))

for i in range(0, n):
    if seats[i] == 1:
        continue
    else:
        seats[i] = 1
        posisions = []
        distance = []

        for j, elem in enumerate(seats):
            if elem == 1:
                posisions.append(j)
        
        for j in range(len(posisions) - 1):
            distance.append(posisions[j + 1] - posisions[j])
        
        seats[i] = 0
        min_distance.append(min(distance))

print(max(min_distance))