def in_range(x, y):
    return 0 <= x and x < 19 and 0 <= y and y < 19

_list = [
    list(map(int, input().split()))
    for _ in range(19)
]

find_answer = 0

for i in range(19):
    if find_answer:
        break
    for j in range(19):
        if find_answer:
            break

        if _list[i][j] == 1:
            if in_range(i, j + 1) and _list[i][j + 1] == 1:
                for k in range(2, 5):
                    if in_range(i, j + k) and _list[i][j + k] == 1:
                        find_answer = 1
                    else:
                        find_answer = 0
                        break

                if find_answer:
                    print(find_answer)
                    print(i + 1, j + 3)

            if in_range(i + 1, j + 1) and _list[i + 1][j + 1] == 1:
                for k in range(2, 5):
                    if in_range(i + k, j + k) and _list[i + k][j + k] == 1:
                        find_answer = 1
                    else:
                        find_answer = 0
                        break

                if find_answer:
                    print(find_answer)
                    print(i + 3, j + 3)

            if in_range(i + 1, j) and _list[i + 1][j] == 1:
                for k in range(2, 5):
                    if in_range(i + k, j) and _list[i + k][j] == 1:
                        find_answer = 1
                    else:
                        find_answer = 0
                        break

                if find_answer:
                    print(find_answer)
                    print(i + 3, j + 1)

        elif _list[i][j] == 2:
            if in_range(i, j + 1) and _list[i][j + 1] == 2:
                for k in range(2, 5):
                    if in_range(i, j + k) and _list[i][j + k] == 2:
                        find_answer = 2
                    else:
                        find_answer = 0
                        break

                if find_answer:
                    print(find_answer)
                    print(i + 1, j + 3)

            if in_range(i + 1, j + 1) and _list[i + 1][j + 1] == 2:
                for k in range(2, 5):
                    if in_range(i + k, j + k) and _list[i + k][j + k] == 2:
                        find_answer = 2
                    else:
                        find_answer = 0
                        break

                if find_answer:
                    print(find_answer)
                    print(i + 3, j + 3)

            if in_range(i + 1, j) and _list[i + 1][j] == 2:
                for k in range(2, 5):
                    if in_range(i + k, j) and _list[i + k][j] == 2:
                        find_answer = 2
                    else:
                        find_answer = 0
                        break

                if find_answer:
                    print(find_answer)
                    print(i + 3, j + 1)

if not find_answer:
    print("0")