s = input()
q_str = input()

q_arr = list(q_str)

for q in q_arr:
    if q == 'L':
        s = s[1:] + s[0]
    elif q == 'R':
        s = s[-1] + s[:-1]

print(s)