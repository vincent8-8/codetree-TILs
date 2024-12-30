n = int(input())
_list = [list(input().split()) for _ in range(n)]

a_score = 0
b_score = 0
top_rating = ''
answer = 0

for person, score in _list:
    score = int(score)
    
    if person == 'A':
        a_score += score
    else:
        b_score += score

    if a_score == b_score:
        if top_rating == "A, B":
            pass
        else:
            answer += 1
            top_rating = "A , B"
    elif a_score < b_score:
        if top_rating == 'B':
            pass
        else:
            answer += 1
            top_rating = 'B'
    else:
        if top_rating == 'A':
            pass
        else:
            answer += 1
            top_rating = 'A'

print(answer)