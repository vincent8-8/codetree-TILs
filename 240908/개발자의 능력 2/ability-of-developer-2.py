import sys

_list = list(map(int, input().split()))

final_min_diff = sys.maxsize


def calc(i, j, k, l):
    remains = [0, 1, 2, 3, 4, 5]
    remains.remove(i)
    remains.remove(j)
    remains.remove(k)
    remains.remove(l)

    team_1 = _list[i] + _list[j]
    team_2 = _list[k] + _list[l]
    team_3 = _list[remains[0]] + _list[remains[1]]

    return abs(max(team_1, team_2, team_3) - min(team_1, team_2, team_3))


for i in range(6):
    for j in range(6):
        for k in range(6):
            for l in range(6):
                if i == j or i == k or i == l or j == k or j == l or k == l:
                    continue
                diff = calc(i, j, k, l)
                if diff < final_min_diff:
                    final_min_diff = diff
print(final_min_diff)