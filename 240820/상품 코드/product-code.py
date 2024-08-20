class C:
    def __init__(self, name = "codetree", code = "50"):
        self.name = name
        self.code = code

name, code = input().split()

c1 = C()
print(f"product {c1.code} is {c1.name}")

c1.name = name
c1.code = code
print(f"product {c1.code} is {c1.name}")