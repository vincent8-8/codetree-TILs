distance = int(input())
time = 1

while True:
    d = 0

    for i in range(1, time // 2 + 1):
        d += i * 2
    
    if time % 2 != 0:
        d += time // 2 + 1

    if d == distance:
        break
    elif d == (distance - 1):
        time += 1
        break

    if time > distance:
        break

    time += 1

print(time)