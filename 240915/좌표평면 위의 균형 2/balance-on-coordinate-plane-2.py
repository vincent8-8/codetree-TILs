import sys

n = int(input())
_list = [
    list(map(int, input().split()))
    for _ in range(n)
]

min_answer = sys.maxsize

for i in range(2, 101, 2):
    for j in range(2, 101, 2):
        _1_quadrant = 0
        _2_quadrant = 0
        _3_quadrant = 0
        _4_quadrant = 0
        local_max = 0

        for x, y in _list:
            if x > i and y > j:
                _1_quadrant += 1
            elif x < i and y > j:
                _2_quadrant += 1
            elif x < i and y < j:
                _3_quadrant += 1
            else:
                _4_quadrant += 1

        local_max = max(_1_quadrant, _2_quadrant, _3_quadrant, _4_quadrant)
        min_answer = min(min_answer, local_max)
        
print(min_answer)