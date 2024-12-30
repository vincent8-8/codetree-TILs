n = int(input())
_input = input()
newbie = 0
curr_people = []
seats = []

for i in range(len(_input)):
    seats.append(int(_input[i]))

for i, elem in enumerate(seats):
    if elem == 1:
        curr_people.append(i)

distance = []

for i in range(len(curr_people) - 1):
    distance.append(curr_people[i + 1] - curr_people[i])

max_distance = max(distance)

for i, elem in enumerate(distance):
    if elem == max_distance:
        newbie = (curr_people[i] + curr_people[i + 1]) // 2

seats[newbie] = 1
distance_after = []
curr_people = []

for i, elem in enumerate(seats):
    if elem == 1:
        curr_people.append(i)

for i in range(len(curr_people) - 1):
    distance_after.append(curr_people[i + 1] - curr_people[i])

print(min(distance_after))