class C:
    def __init__(self, c_name = "", score = 0):
        self.c_name = c_name
        self.score = score
    
_list = [
    tuple(input().split())
    for _ in range(5)
]

students = [C() for _ in range(5)]
min_score = 100
index = 0

for i in range(5):
    c_name, score = _list[i]
    students[i].c_name = c_name
    students[i].score = int(score)
    if students[i].score < min_score:
        min_score = students[i].score
        index = i


print(students[index].c_name, students[index].score)