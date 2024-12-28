distance = int(input())
min_time = distance

for time in range(1, distance):
    d = 0
    extra_time = 0

    for i in range(1, time // 2 + 1):
        d += i * 2

    if time % 2 != 0:
        d += time // 2 + 1


    if d < distance:
        remaining_distance = distance - d

        for i in range(time // 2, 0, -1):
            cut = remaining_distance // i

            if cut >= 1:
                remaining_distance -= cut * i
                d += cut * i
                extra_time += cut

    if d == distance:
        min_time = min(min_time, time + extra_time)

print(min_time)