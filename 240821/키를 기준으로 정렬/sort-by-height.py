n = int(input())

class People:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []

for _ in range(n):
    name, height, weight = tuple(input().split())
    people.append(People(name, height, weight))

people.sort(key=lambda x: x.height)

for i in range(n):
    print(people[i].name, people[i].height, people[i].weight)