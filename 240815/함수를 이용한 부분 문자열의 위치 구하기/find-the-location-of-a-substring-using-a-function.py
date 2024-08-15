s = input()
t = input()

def i_return():
    if t in s:
        return s.find(t)

print(i_return())