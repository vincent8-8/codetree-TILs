n = int(input())
_list = [
    tuple(input().split())
    for _ in range(n)
]

class Day:
    def __init__(self, date="",  w_day="", weather=""):
        self.date = date
        self.w_day = w_day
        self.weather = weather

days = [Day() for _ in range(n)]
r_days = []

for i in range(n):
    date, w_day, weather = _list[i]

    days[i].date = date
    days[i].w_day = w_day
    days[i].weather = weather

    if days[i].weather == "Rain":
        r_days.append(days[i])

index = 0

if len(r_days) == 1:
    pass
else:
    for i in range(len(r_days) - 1):
        if r_days[i].date < r_days[i + 1].date:
            index = i
        else:
            index = i + 1

print(r_days[index].date, r_days[index].w_day, r_days[index].weather)