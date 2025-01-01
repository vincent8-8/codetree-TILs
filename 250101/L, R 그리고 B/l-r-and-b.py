_graph = [input() for _ in range(10)]
bx = 0
by = 0
rx = 0
ry = 0
lx = 0
ly = 0
distance = 0

for row in range(10):
    for column in range(10):
        if _graph[row][column] == 'B':
            bx = row
            by = column
        elif _graph[row][column] == 'L':
            lx = row
            ly = column
        elif _graph[row][column] == 'R':
            rx = row
            ry = column

if bx == lx:
    if bx == rx:
        if bx < rx < lx or lx < rx < bx:
            distance = abs(by - ly) + 1
        else:
            distance = abs(by - ly) - 1
    else:
        distance = abs(by - ly) - 1
elif by == ly:
    if by == ry:
        if by < ry < ly or ly < ry < by:
            distance = abs(bx - lx) + 1
        else:
            distance = abs(bx - lx) - 1
    else:
        distance = abs(bx - ly) - 1
else:
    distance = abs(bx - lx) + abs(by - ly) - 1

print(distance)