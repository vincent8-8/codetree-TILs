n, k = map(int, input().split())
_list = list("" for _ in range(10000))
max_score = 0

for _ in range(n):
    idx, alph = input().split()
    _list[int(idx) - 1] = alph

for i in range(10000 - k):
    score = 0
    for j in range(i, i + k + 1):
        if _list[j] == "G":
            score += 1
        elif _list[j] == "H":
            score += 2
    if score != 0:
        max_score = max(max_score, score)

print(max_score)