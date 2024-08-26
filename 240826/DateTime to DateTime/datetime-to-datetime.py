a, b, c = map(int, input().split())

minutes = ((a - 11) * 24 * 60 + b * 60 + c ) - (11 * 60 + 11)
print(minutes)