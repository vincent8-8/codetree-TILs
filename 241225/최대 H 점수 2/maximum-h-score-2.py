n, l = map(int, input().split())
_list = list(map(int, input().split()))
h_score = 0

for i in range(1, 101):
    shift_counter = l
    counter = 0

    for elem in _list:
        if elem >= i:
            counter += 1
        elif elem == (i - 1) and shift_counter >= 1:
            counter += 1
            shift_counter -= 1

    if counter >= i:
         h_score = i

print(h_score)


