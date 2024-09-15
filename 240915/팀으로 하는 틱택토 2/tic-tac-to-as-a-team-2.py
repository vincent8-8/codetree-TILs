_graph = [
    input()
    for _ in range(3)
]

cnt = 0
sets = []

for i in range(3):
    sets.append(set((_graph[i][0], _graph[i][1], _graph[i][2])))
    sets.append(set((_graph[0][i], _graph[1][i], _graph[2][i])))
        
sets.append(set((_graph[0][0], _graph[1][1], _graph[2][2])))
sets.append(set((_graph[2][2], _graph[1][1], _graph[2][0])))

answer_list = []

for i in range(len(sets)):
    if len(sets[i]) == 2 and not(sets[i] in answer_list):
        answer_list.append(sets[i])

print(len(answer_list))