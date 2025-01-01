n = int(input())
_list = [list(input().split()) for _ in range(n)]
count = 0
rating = [0, 1, 2]

people = [0, 0, 0]

for person, score in _list:
    score = int(score)

    if person == 'A':
        people[0] += score
    elif person == 'B':
        people[1] += score
    else:
        people[2] += score
    
    max_score = max(people)
    rating_local = []

    for i in range(3):
        if people[i] == max_score:
            rating_local.append(i)
        
    if rating == rating_local:
        pass
    else:
        count += 1
        rating = rating_local

print(count)