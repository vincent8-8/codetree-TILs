s, q = input().split()

questions = [
    list(input().split())
    for _ in range(int(q))
]

for question in questions:
    if question[0] == '1':
        tmp_arr = list(s)
        a = int(question[1]) - 1
        b = int(question[2]) - 1

        tmp = tmp_arr[a]
        tmp_arr[a] = tmp_arr[b]
        tmp_arr[b] = tmp
        print("".join(tmp_arr))

    else:
        a = question[1]
        b = question[2]
        tmp_arr = list(s)

        for i in range(0, len(tmp_arr)):
            if tmp_arr[i] == a:
                tmp_arr[i] = b
        print("".join(tmp_arr))