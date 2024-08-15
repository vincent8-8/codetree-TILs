s = input()
t = input()

def i_return():
    if t in s:
        return s.find(t)
    else:
        return -1

print(i_return())