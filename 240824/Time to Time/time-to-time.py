a, b, c, d = map(int, input().split())

elapsed_a = a * 60 + b
elapsed_b = c * 60 + d

elapsed_t = elapsed_b - elapsed_a
print(elapsed_t)