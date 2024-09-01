def in_range(x, y):
    return 0 <= x and x < r and 0 <= y and y < c:

r, c = map(int, input().split())
_list = [
    list(input().split())
    for _ in range(r)
]

curr_color = _list[0][0]