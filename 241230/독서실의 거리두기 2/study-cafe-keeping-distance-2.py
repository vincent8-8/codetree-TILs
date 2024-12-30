n = int(input())
_input = input()
curr_people = []
seats = []

for i in range(len(_input)):
    seats.append(int(_input[i]))

for i, elem in enumerate(seats):
    if elem == 1:
        curr_people.append(i)

seats[0] = 1
seats[-1] = 1

for i in range(len(curr_people) - 1):
    new_person = (curr_people[i + 1] - curr_people[i]) // 2
    seats[new_person] = 1

curr_people = []
distance = []

for i, elem in enumerate(seats):
    if elem == 1:
        curr_people.append(i)

for i in range(len(curr_people) - 1):
    distance.append(curr_people[i + 1] - curr_people[i])

print(max(distance))