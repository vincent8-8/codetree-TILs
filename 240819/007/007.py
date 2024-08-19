s, l, n = input().split()

class C:
    def __init__(self, s, l, n):
        self.s = s
        self.l = l
        self.n = n

c1 = C(s, l, n)
print(f"secret code : {c1.s}")
print(f"meeting point : {c1.l}")
print(f"time : {c1.n}")