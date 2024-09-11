n, k = map(int, input().split())
_list = [
    int(input())
    for _ in range(n)
]

max_bomb = 0

for i in range(n):
    curr_bomb = _list[i]
    for j in range(i + 1, n):
        explode_bomb = 0
        if curr_bomb == _list[j]:
            if (j - i) <= k:
                explode_bomb = curr_bomb
            
        max_bomb = max(max_bomb, explode_bomb)
print(max_bomb)