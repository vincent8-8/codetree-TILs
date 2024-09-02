n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_diff  = -1
target_index = -1

for i in range(1, n - 1):
    before = abs(_list[i - 1][0] - _list[i][0]) + abs(_list[i - 1][1] - _list[i][1]) + abs(_list[i][0] - _list[i + 1][0]) + abs(_list[i][1] - _list[i + 1][1])
    after = abs(_list[i - 1][0] - _list[i + 1][0]) + abs(_list[i - 1][1] - _list[i + 1][1])
    
    diff = before - after

    if diff > max_diff:
        max_diff = diff
        target_index = i
    
result_distance = 0

for i in range(n - 1):
    if (i + 1) == target_index:
        result_distance += abs(_list[i][0] - _list[i + 2][0]) + abs(_list[i][1] - _list[i + 2][1])
    elif i == target_index:
        continue    
    else:
        result_distance += abs(_list[i][0] - _list[i + 1][0]) + abs(_list[i][1] - _list[i + 1][1])

print(result_distance)