n, k = map(int, input().split())
_list = list(map(int, input().split()))

def is_possible(num):
    available_indices = []
    for i, elem in enumerate(_list):
        if elem <= num :
            available_indices.append(i)

    for j in range(0, len(available_indices) - 1):
        if available_indices[j + 1] - available_indices[j] > k:
            return False
    return True


minOfMax = 0

for num in range(max(_list[0], _list[-1]), 101):
    if is_possible(num):
        minOfMax = num
        break

print(minOfMax)
