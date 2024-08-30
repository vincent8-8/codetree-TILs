N, K ,P, T = map(int, input().split())

_list = [0] * (N + 1)

_list[P] = 2 * K - 1

q = []

for _ in range(T):
    t, x, y = map(int, input().split())
    q.append((t, x, y))

q.sort(key=lambda x: x[0])

for _, x, y in q:
    if _list[x] != 0:                # 1.   if x was addicted
        if _list[y] == 0:            # 1-1. if y was not addicted
            if _list[x] > 0:
                _list[x] -= 2
                _list[y] = 2 * K - 1
        else:                        # 1-2.  if y was also addicted
            _list[x] -= 2
            _list[y] -= 2
    else:                            # 2.  if x was not addicted
        if _list[y] != 0:            # 2-1. if y was addicted
            if _list[y] > 0:
                _list[y] -= 2
                _list[x] = 2 * K - 1

infectees = [0] * (N + 1)

for i in range(1, N + 1):
    if _list[i] != 0:
        infectees[i] = 1
    print(infectees[i], end="")