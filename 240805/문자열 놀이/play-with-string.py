s, q = input().split()

questions = [
    list(input().split())
    for _ in range(int(q))
]

arr = list(s)

for question in questions:
    if question[0] == '1':
        a = int(question[1]) - 1
        b = int(question[2]) - 1

        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp
        print("".join(arr))

    else:
        a = question[1]
        b = question[2]

        for i in range(0, len(arr)):
            if arr[i] == a:
                arr[i] = b
        print("".join(arr))