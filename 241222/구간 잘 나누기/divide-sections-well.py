from itertools import combinations
import sys

n, m = map(int, input().split())
_list = list(map(int, input().split()))

# 정답 저장 변수
min_of_max = sys.maxsize


# 문제에서 주어진 숫자의 개수 만큼 가능한 파티션의 위치를 리스트로 생성
possible_partition_index = [i + 1 for i in range(n - 1)]

_partitions = list(combinations(possible_partition_index, m - 1))

for partitions in _partitions:
    local_max = 0

    for i in range(m):
        local_sum = 0

        if i == 0:
            local_sum = sum(_list[: partitions[i]])
        elif i == m - 1:
            local_sum = sum(_list[partitions[i - 1] : ])
        else:
            local_sum = sum(_list[partitions[i - 1] : partitions[i]])

        local_max = max(local_max, local_sum)
        
    min_of_max = min(min_of_max, local_max)

print(min_of_max)