class C:
    def __init__(self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()

c1 = C(code, color, sec)
print(f"code : {c1.code}")
print(f"color : {c1.color}")
print(f"second : {c1.sec}")